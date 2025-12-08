# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PlayerParam"]


class PlayerParam(TypedDict, total=False):
    """Set of properties for displaying videos.

    All parameters may be blank to inherit their values from default Streaming player.
    """

    name: Required[str]
    """Player name"""

    id: int
    """Player ID"""

    autoplay: bool
    """Enables video playback right after player load:

    - **true** — video starts playing right after player loads
    - **false** — video isn’t played automatically. A user must click play to start

    Default is false
    """

    bg_color: str
    """Color of skin background in format #AAAAAA"""

    client_id: int
    """Client ID"""

    custom_css: str
    """Custom CSS to be added to player iframe"""

    design: str
    """String to be rendered as JS parameters to player"""

    disable_skin: bool
    """Enables/Disables player skin:

    - **true** — player skin is disabled
    - **false** — player skin is enabled

    Default is false
    """

    fg_color: str
    """Color of skin foreground (elements) in format #AAAAAA"""

    framework: str
    """Player framework type"""

    hover_color: str
    """Color of foreground elements when mouse is over in format #AAAAAA"""

    js_url: str
    """Player main JS file URL. Leave empty to use JS URL from the default player"""

    logo: str
    """URL to logo image"""

    logo_position: str
    """Logotype position.
     Has four possible values:

    - **tl** — top left
    - **tr** — top right
    - **bl** — bottom left
    - **br** — bottom right

    Default is null
    """

    mute: bool
    """Regulates the sound volume:

    - **true** — video starts with volume off
    - **false** — video starts with volume on

    Default is false
    """

    save_options_to_cookies: bool
    """Enables/Disables saving volume and other options in cookies:

    - **true** — user settings will be saved
    - **false** — user settings will not be saved

    Default is true
    """

    show_sharing: bool
    """Enables/Disables sharing button display:

    - **true** — sharing button is displayed
    - **false** — no sharing button is displayed

    Default is true
    """

    skin_is_url: str
    """URL to custom skin JS file"""

    speed_control: bool
    """Enables/Disables speed control button display:

    - **true** — sharing button is displayed
    - **false** — no sharing button is displayed

    Default is false
    """

    text_color: str
    """Color of skin text elements in format #AAAAAA"""
