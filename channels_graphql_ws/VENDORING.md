# GraphQL WebSocket implementation

This directory vendors the `channels_graphql_ws` Python package from
`silverlogic/DjangoChannelsGraphqlWs` at commit
`b34ef1aae9a5b16683dc61d0488055502787ec84` (the `baseapp-django-channels-graphql-ws`
1.0.0rc9 source). The original copyright notices remain in the files, and the
MIT license is included as `LICENSE`.

The upstream package pins `graphql-core==3.2.3`. We package its source here so
the application's GraphQL extra can require a patched `graphql-core` 3.2
release. Any future update of this directory must be reviewed against the
upstream source and the project's WebSocket subscription tests.
