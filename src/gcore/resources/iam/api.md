# Iam

Types:

```python
from gcore.types.iam import AccountOverview
```

Methods:

- <code title="get /iam/clients/me">client.iam.<a href="./src/gcore/resources/iam/iam.py">get_account_overview</a>() -> <a href="./src/gcore/types/iam/account_overview.py">AccountOverview</a></code>

## APITokens

Types:

```python
from gcore.types.iam import APIToken, APITokenCreated, APITokenList
```

Methods:

- <code title="post /iam/clients/{clientId}/tokens">client.iam.api_tokens.<a href="./src/gcore/resources/iam/api_tokens.py">create</a>(client_id, \*\*<a href="src/gcore/types/iam/api_token_create_params.py">params</a>) -> <a href="./src/gcore/types/iam/api_token_created.py">APITokenCreated</a></code>
- <code title="get /iam/clients/{clientId}/tokens">client.iam.api_tokens.<a href="./src/gcore/resources/iam/api_tokens.py">list</a>(client_id, \*\*<a href="src/gcore/types/iam/api_token_list_params.py">params</a>) -> <a href="./src/gcore/types/iam/api_token_list.py">APITokenList</a></code>
- <code title="delete /iam/clients/{clientId}/tokens/{tokenId}">client.iam.api_tokens.<a href="./src/gcore/resources/iam/api_tokens.py">delete</a>(token_id, \*, client_id) -> None</code>
- <code title="get /iam/clients/{clientId}/tokens/{tokenId}">client.iam.api_tokens.<a href="./src/gcore/resources/iam/api_tokens.py">get</a>(token_id, \*, client_id) -> <a href="./src/gcore/types/iam/api_token.py">APIToken</a></code>

## Users

Types:

```python
from gcore.types.iam import User, UserDetailed, UserInvite, UserUpdated
```

Methods:

- <code title="patch /iam/users/{userId}">client.iam.users.<a href="./src/gcore/resources/iam/users.py">update</a>(user_id, \*\*<a href="src/gcore/types/iam/user_update_params.py">params</a>) -> <a href="./src/gcore/types/iam/user_updated.py">UserUpdated</a></code>
- <code title="get /iam/users">client.iam.users.<a href="./src/gcore/resources/iam/users.py">list</a>(\*\*<a href="src/gcore/types/iam/user_list_params.py">params</a>) -> <a href="./src/gcore/types/iam/user.py">SyncOffsetPage[User]</a></code>
- <code title="delete /iam/clients/{clientId}/client-users/{userId}">client.iam.users.<a href="./src/gcore/resources/iam/users.py">delete</a>(user_id, \*, client_id) -> None</code>
- <code title="get /iam/users/{userId}">client.iam.users.<a href="./src/gcore/resources/iam/users.py">get</a>(user_id) -> <a href="./src/gcore/types/iam/user_detailed.py">UserDetailed</a></code>
- <code title="post /iam/clients/invite_user">client.iam.users.<a href="./src/gcore/resources/iam/users.py">invite</a>(\*\*<a href="src/gcore/types/iam/user_invite_params.py">params</a>) -> <a href="./src/gcore/types/iam/user_invite.py">UserInvite</a></code>
