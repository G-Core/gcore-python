# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Player"]


class Player(BaseModel):
    """Set of properties for displaying videos.

    All parameters may be blank to inherit their values from default Streaming player.
    """

    name: str
    """Player name"""

    id: Optional[int] = None
    """Player ID"""

    autoplay: Optional[bool] = None
    """Enables video playback right after player load:

    - **true** — video starts playing right after player loads
    - **false** — video isn’t played automatically. A user must click play to start

    Default is false
    """

    bg_color: Optional[str] = None
    """Color of skin background in format #AAAAAA"""

    client_id: Optional[int] = None
    """Client ID"""

    custom_css: Optional[str] = None
    """Custom CSS to be added to player iframe"""

    design: Optional[str] = None
    """String to be rendered as JS parameters to player"""

    disable_skin: Optional[bool] = None
    """Enables/Disables player skin:

    - **true** — player skin is disabled
    - **false** — player skin is enabled

    Default is false
    """

    fg_color: Optional[str] = None
    """Color of skin foreground (elements) in format #AAAAAA"""

    framework: Optional[str] = None
    """Player framework type"""

    hover_color: Optional[str] = None
    """Color of foreground elements when mouse is over in format #AAAAAA"""

    js_url: Optional[str] = None
    """Player main JS file URL. Leave empty to use JS URL from the default player"""

    logo: Optional[str] = None
    """URL to logo image"""

    logo_position: Optional[str] = None
    """Logotype position.
     Has four possible values:

    - **tl** — top left
    - **tr** — top right
    - **bl** — bottom left
    - **br** — bottom right

    Default is null
    """

    mute: Optional[bool] = None
    """Regulates the sound volume:

    - **true** — video starts with volume off
    - **false** — video starts with volume on

    Default is false
    """

    save_options_to_cookies: Optional[bool] = None
    """Enables/Disables saving volume and other options in cookies:

    - **true** — user settings will be saved
    - **false** — user settings will not be saved

    Default is true
    """

    show_sharing: Optional[bool] = None
    """Enables/Disables sharing button display:

    - **true** — sharing button is displayed
    - **false** — no sharing button is displayed

    Default is true
    """

    skin_is_url: Optional[str] = None
    """URL to custom skin JS file"""

    speed_control: Optional[bool] = None
    """Enables/Disables speed control button display:

    - **true** — sharing button is displayed
    - **false** — no sharing button is displayed

    Default is false
    """

    text_color: Optional[str] = None
    """Color of skin text elements in format #AAAAAA"""
