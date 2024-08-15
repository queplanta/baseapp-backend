import graphene
import swapper
from baseapp_core.graphql import (
    RelayMutation,
    SerializerMutation,
    get_object_type_for_model,
    get_pk_from_relay_id,
    login_required,
)
from baseapp_pages.models import URLPath
from django.utils.translation import gettext_lazy as _
from graphql.error import GraphQLError
from rest_framework import serializers

Profile = swapper.load_model("baseapp_profiles", "Profile")


class BaseProfileSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    name = serializers.CharField(required=False)
    image = serializers.ImageField(required=False)
    banner_image = serializers.ImageField(required=False)
    url_path = serializers.SlugField(required=False)

    class Meta:
        model = Profile
        fields = ("owner", "name", "image", "banner_image", "biography", "url_path")

    def validate_url_path(self, value):
        if URLPath.objects.filter(path=value).exists():
            raise serializers.ValidationError(
                _("URL path already in use, please choose another one")
            )
        return value


class ProfileCreateSerializer(BaseProfileSerializer):
    name = serializers.CharField(required=True)
    target = serializers.CharField(required=True)

    class Meta(BaseProfileSerializer.Meta):
        fields = BaseProfileSerializer.Meta.fields + ("target",)

    def create(self, validated_data):
        url_path = validated_data.pop("url_path", None)
        instance = super().create(validated_data)
        if url_path:
            URLPath.objects.create(path=url_path, target=instance, is_active=True)
        return instance


class ProfileUpdateSerializer(BaseProfileSerializer):
    def update(self, instance, validated_data):
        url_path = validated_data.pop("url_path", None)
        instance = super().update(instance, validated_data)
        if url_path:
            instance.url_paths.all().delete()
            URLPath.objects.create(path=url_path, target=instance, is_active=True)
        return instance


class ProfileCreate(SerializerMutation):
    profile = graphene.Field(lambda: Profile.get_graphql_object_type()._meta.connection.Edge)

    class Meta:
        serializer_class = ProfileCreateSerializer

    @classmethod
    @login_required
    def mutate_and_get_payload(cls, root, info, **input):
        if not info.context.user.has_perm("baseapp_profiles.add_profile"):
            raise GraphQLError(
                str(_("You don't have permission to perform this action")),
                extensions={"code": "permission_required"},
            )

        return super().mutate_and_get_payload(root, info, **input)

    @classmethod
    def perform_mutate(cls, serializer, info):
        ProfileObjectType = Profile.get_graphql_object_type()
        # TODO: get target using get_obj_from_relay_id and inject into the serializer to be used
        # by validate and create methods
        obj = serializer.save()
        return cls(
            errors=None,
            profile=ProfileObjectType._meta.connection.Edge(node=obj),
        )


class ProfileUpdate(SerializerMutation):
    profile = graphene.Field(get_object_type_for_model(Profile))

    class Meta:
        serializer_class = ProfileUpdateSerializer

    class Input:
        id = graphene.ID(required=True)

    @classmethod
    def get_serializer_kwargs(cls, root, info, id, **input):
        kwargs = super().get_serializer_kwargs(root, info, **input)
        input = kwargs["data"]

        try:
            pk = get_pk_from_relay_id(id)
            instance = Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            raise ValueError(_("Profile not found"))

        if not info.context.user.has_perm("baseapp_profiles.change_profile", instance):
            raise GraphQLError(
                str(_("You don't have permission to perform this action")),
                extensions={"code": "permission_required"},
            )

        return {
            "instance": instance,
            "data": input,
            "partial": True,
            "context": {"request": info.context},
        }

    @classmethod
    def perform_mutate(cls, serializer, info):
        obj = serializer.save()
        return cls(
            errors=None,
            profile=obj,
        )

    @classmethod
    @login_required
    def mutate_and_get_payload(cls, root, info, **input):
        return super().mutate_and_get_payload(root, info, **input)


class ProfileDelete(RelayMutation):
    deleted_id = graphene.ID()

    class Input:
        id = graphene.ID(required=True)

    @classmethod
    @login_required
    def mutate_and_get_payload(cls, root, info, **input):
        relay_id = input.get("id")
        pk = get_pk_from_relay_id(relay_id)

        try:
            obj = Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            obj = None

        error_exception = GraphQLError(
            str(_("You don't have permission to perform this action")),
            extensions={"code": "permission_required"},
        )
        if not obj:
            raise error_exception

        if not info.context.user.has_perm("baseapp_profiles.delete_profile", obj):
            raise error_exception

        obj.delete()

        return ProfileDelete(deleted_id=relay_id)


class ProfilesMutations(object):
    # profile_create = ProfileCreate.Field()
    profile_update = ProfileUpdate.Field()
    profile_delete = ProfileDelete.Field()
