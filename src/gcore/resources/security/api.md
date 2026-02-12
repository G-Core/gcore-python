# Security

## Events

Types:

```python
from gcore.types.security import ClientView
```

Methods:

- <code title="get /security/notifier/v1/event_logs">client.security.events.<a href="./src/gcore/resources/security/events.py">list</a>(\*\*<a href="src/gcore/types/security/event_list_params.py">params</a>) -> <a href="./src/gcore/types/security/client_view.py">SyncOffsetPage[ClientView]</a></code>

## BgpAnnounces

Types:

```python
from gcore.types.security import ClientAnnounce, BgpAnnounceListResponse
```

Methods:

- <code title="get /security/sifter/v2/protected_addresses/announces">client.security.bgp_announces.<a href="./src/gcore/resources/security/bgp_announces.py">list</a>(\*\*<a href="src/gcore/types/security/bgp_announce_list_params.py">params</a>) -> <a href="./src/gcore/types/security/bgp_announce_list_response.py">BgpAnnounceListResponse</a></code>
- <code title="post /security/sifter/v2/protected_addresses/announces">client.security.bgp_announces.<a href="./src/gcore/resources/security/bgp_announces.py">toggle</a>(\*\*<a href="src/gcore/types/security/bgp_announce_toggle_params.py">params</a>) -> object</code>

## ProfileTemplates

Types:

```python
from gcore.types.security import ClientProfileTemplate, ProfileTemplateListResponse
```

Methods:

- <code title="get /security/iaas/profile-templates">client.security.profile_templates.<a href="./src/gcore/resources/security/profile_templates.py">list</a>() -> <a href="./src/gcore/types/security/profile_template_list_response.py">ProfileTemplateListResponse</a></code>

## Profiles

Types:

```python
from gcore.types.security import ClientProfile, ProfileListResponse
```

Methods:

- <code title="post /security/iaas/v2/profiles">client.security.profiles.<a href="./src/gcore/resources/security/profiles.py">create</a>(\*\*<a href="src/gcore/types/security/profile_create_params.py">params</a>) -> <a href="./src/gcore/types/security/client_profile.py">ClientProfile</a></code>
- <code title="get /security/iaas/v2/profiles">client.security.profiles.<a href="./src/gcore/resources/security/profiles.py">list</a>(\*\*<a href="src/gcore/types/security/profile_list_params.py">params</a>) -> <a href="./src/gcore/types/security/profile_list_response.py">ProfileListResponse</a></code>
- <code title="delete /security/iaas/v2/profiles/{id}">client.security.profiles.<a href="./src/gcore/resources/security/profiles.py">delete</a>(id) -> None</code>
- <code title="get /security/iaas/v2/profiles/{id}">client.security.profiles.<a href="./src/gcore/resources/security/profiles.py">get</a>(id) -> <a href="./src/gcore/types/security/client_profile.py">ClientProfile</a></code>
- <code title="put /security/iaas/v2/profiles/{id}/recreate">client.security.profiles.<a href="./src/gcore/resources/security/profiles.py">recreate</a>(id, \*\*<a href="src/gcore/types/security/profile_recreate_params.py">params</a>) -> <a href="./src/gcore/types/security/client_profile.py">ClientProfile</a></code>
- <code title="put /security/iaas/v2/profiles/{id}">client.security.profiles.<a href="./src/gcore/resources/security/profiles.py">replace</a>(id, \*\*<a href="src/gcore/types/security/profile_replace_params.py">params</a>) -> <a href="./src/gcore/types/security/client_profile.py">ClientProfile</a></code>
