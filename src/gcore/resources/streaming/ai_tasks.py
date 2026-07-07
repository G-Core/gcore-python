# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, overload

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, required_args, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncPageStreamingAI, AsyncPageStreamingAI
from ..._base_client import AsyncPaginator, make_request_options
from ...types.streaming import ai_task_list_params, ai_task_create_params, ai_task_get_ai_settings_params
from ...types.streaming.ai_task import AITask
from ...types.streaming.ai_task_get_response import AITaskGetResponse
from ...types.streaming.ai_task_cancel_response import AITaskCancelResponse
from ...types.streaming.ai_task_create_response import AITaskCreateResponse
from ...types.streaming.ai_task_get_ai_settings_response import AITaskGetAISettingsResponse

__all__ = ["AITasksResource", "AsyncAITasksResource"]


class AITasksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AITasksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AITasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AITasksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AITasksResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        task_name: Literal["transcription"],
        url: str,
        audio_language: str | Omit = omit,
        client_entity_data: str | Omit = omit,
        client_user_id: str | Omit = omit,
        subtitles_language: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AITaskCreateResponse:
        """
        Creating an AI task.

        This method allows you to create an AI task for VOD video processing:

        - ASR: Transcribe video
        - ASR: Translate subtitles
        - CM: Sports detection
        - CM: Not Safe For Work (NSFW) content detection
        - CM: Soft nudity detection
        - CM: Hard nudity detection
        - CM: Objects recognition (soon)

        ![Auto generated subtitles example](https://demo-files.gvideo.io/apidocs/captions.gif)

        How to use:

        - Create an AI task, specify algorithm to use
        - Get `task_id`
        - Check a result using `.../ai/tasks/{task_id}` method

        For more detailed information, see the algorithm-specific sections below.

        **AI Automatic Speech Recognition (ASR)**

        AI is instrumental in automatic video processing for subtitles creation by using
        Automatic Speech Recognition (ASR) technology to transcribe spoken words into
        text, which can then be translated into multiple languages for broader
        accessibility.

        Categories:

        - `transcription` – to create subtitles/captions from audio in the original
          language.
        - `translation` – to translate subtitles/captions from the original language to
          99+ other languages.

        AI subtitle transcription and translation tools are highly efficient, processing
        large volumes of audio-visual content quickly and providing accurate
        transcriptions and translations with minimal human intervention. Additionally,
        AI-driven solutions can significantly reduce costs and turnaround times compared
        to traditional methods, making them an invaluable resource for content creators
        and broadcasters aiming to reach global audiences.

        Example response with positive result:

        ```
        {
          "status": "SUCCESS",
          "result": {
            "subtitles": [
              {
                  "start_time": "00:00:00.031",
                  "end_time": "00:00:03.831",
                  "text": "Come on team, ..."
              }, ...
            ]
            "vttContent": "WEBVTT\n\n1\n00:00:00.031 --> 00:00:03.831\nCome on team, ...",
            "concatenated_text": "Come on team, ...",
            "languages": [ "eng" ],
            "speech_detected": true
            }
          }, ...
        }
        ```

        **AI Content Moderation (CM)**

        The AI Content Moderation API offers a powerful solution for analyzing video
        content to detect various categories of inappropriate material. Leveraging
        state-of-the-art AI models, this API ensures real-time analysis and flagging of
        sensitive or restricted content types, making it an essential tool for platforms
        requiring stringent content moderation.

        Categories:

        - `nsfw`: Quick algorithm to detect pornographic material, ensuring content is
          "not-safe-for-work" or normal.
        - `hard_nudity`: Detailed analysis of video which detects explicit nudity
          involving genitalia.
        - `soft_nudity`: Detailed video analysis that reveals both explicit and partial
          nudity, including the presence of male and female faces and other uncovered
          body parts.
        - `sport`: Recognizes various sporting activities.

        The AI Content Moderation API is an invaluable tool for managing and controlling
        the type of content being shared or streamed on your platform. By implementing
        this API, you can ensure compliance with community guidelines and legal
        requirements, as well as provide a safer environment for your users.

        Important notes:

        - It's allowed to analyze still images too (where applicable). Format of image:
          JPEG, PNG. In that case one image is the same as video of 1 second duration.
        - Not all frames in the video are used for analysis, but only key frames
          (Iframe). For example, if a key frame in a video is set every ±2 seconds, then
          detection will only occur at these timestamps. If an object appears and
          disappears between these time stamps, it will not be detected. We are working
          on a version to analyze more frames, please contact your manager or our
          support team to enable this method.

        Example response with positive result:

        ```
        {
          "status": "SUCCESS",
          "result": {
              "nsfw_detected": true,
              "detection_results": [ "nsfw" ],
              "frames": [
                  {
                      "label": "nsfw",
                      "confidence": 1.0,
                      "frame_number": 24
                  },...
              ]
          }
        }
        ```

        **Additional information**

        Billing takes into account the duration of the analyzed video. Or the duration
        until the stop tag(where applicable), if the condition was triggered during the
        analysis.

        The heart of content moderation is AI, with additional services. They run on our
        own infrastructure, so the files/data are not transferred anywhere to external
        services. After processing, original files are also deleted from local storage
        of AI.

        Read more detailed information about our solution, and architecture, and
        benefits in the knowledge base and blog.

        **Algorithm-specific details**

        Create AI ASR task

        Transcribing is the process of writing down the words you hear in an audio. Our
        solution allows you to transcribe audio from your video and get subtitles
        automatically. To do this, we use modern AI models.

        The result:

        - Transcription – subtitles in the original language. I.e. audio is in English –
          subtitles are in English too, audio is in German – subtitles are in German
          too.
        - Translation – subtitles is translated from the original language to any other
          language.

        **How to use?**

        - Explicit call to this AI method. Applicable for any file stored with us or
          located on the Internet.
        - Standard video upload but with automatic subtitle generation. Look at
          ["VOD uploading"](/api-reference/streaming/videos/create-video).

        **What language will the subtitles be in?**

        You can specify the language explicitly, then it will be used to create
        subtitles: the source language in the audio, the resulting subtitle language. If
        this is not set, the system will run auto language identification and the
        subtitles will be in the detected language. The method also works based on AI
        analysis.

        Additionally, when this is not set, we also support recognition of alternate
        languages in the video (code-switching). For example, when in a video different
        speakers speak several languages, or when they switch from their native language
        to English and back. Thus when you have multiple languages in the video it is
        better to not specify an "audio_language" otherwise AI may force the system to
        recognize gibberish.

        **What can be transcribed?**

        Service uses additional methods to detect presence of speech in audio track,
        thus improving the detection of any human conversations:

        - Speech of one speaker,
        - Speech of several speakers,
        - Speech in different languages,
        - etc

        Restriction on music, lyrics most likely will not be created.

        **What about translation?**

        It is also possible to automatically translate from the original language to
        another you need.

        To create a translation, specify the desired language explicitly in
        "subtitles_language" parameter. Otherwise, the subtitles will be in the original
        language. Translation into different languages should be done by creating
        separate tasks.

        ![Auto generated subtitles example](https://demo-files.gvideo.io/apidocs/captions.gif)

        Use MP4 videos to process. This method is not tied to videos that are stored
        only in our video hosting (look at how get a link to MP4 rendition), so you can
        use links to any other external file with HTTP/HTTPS access.

        For now, only the first audio track can be processed; later this functionality
        will be improved to allow to use any. Also, not all language pairs are currently
        supported. If a language pair is not supported for automatic translation, the
        task status will be FAILURE with description of the reason. Example:
        `eng => uzb`. You can request to add the language pair you need for automatic
        translation. Contact our support.

        Example of modes to transcribe and/or translate:

        - Auto language detection: `{ "url":"..." }`
        - From German language explicitly : `{ "url":"...", "audio_language":"ger" }`
        - From any auto-detected to English language explicitly:
          `{ "url":"...", "subtitles_language":"eng" }`
        - From German language to English language explicitly:
          `{ "url":"...", "audio_language":"ger", "subtitles_language":"eng" }`

        Example of setting a task to process MP4 file (animated gif from above):

        ```
        curl -L 'https://api.gcore.com/streaming/ai/tasks' \\
        -H 'Content-Type: application/json' \\
        -H 'Authorization: APIKey 1234$abcd...' \\
        -d '{
            "url": "https://demo-files.gvideo.io/apidocs/spritefright-blender-cut30sec.mp4"
        }'
        ```

        As described above, transcription is done automatically using AI. Therefore, the
        quality may differ from a manual transcription by a professional person. If this
        happens to you, then you can download subtitles and change them in an external
        editor.

        Transcription and translation are 2 different AI tasks:

        - Transcription is set only for transcription.
        - Translation, if non-original languages are set for translation.

        Billing takes into account the duration of the analyzed original video.

        The heart for transcribing is the AI model Whisper from OpenAI, with additional
        optimizations and services. The AI models run on our own infrastructure, so the
        files/data are not transferred anywhere to external services. After processing,
        original files are also deleted from local storage of AI.

        Read more detailed information about our solution, and architecture, and
        benefits in the knowledge base and blog.

        Create AI CM:nsfw task

        This algorithm allows to quickly detect inappropriate content, determining that
        the content is NSFW ("Not Safe For Work") or normal. Generic info about all
        capabilities and limits see in the generic
        ["Content Moderation"](/api-reference/streaming/ai/create-ai-task) method.

        **What is "Not Safe For Work"?**

        The algorithm has recognized inappropriate content in a video and it might not
        be suitable to view in public places. The solution provides its confidence level
        (in percentage) of how sure it is that the content is NSFW, or it most likely
        does not contain any sexual or similar content.

        Different to soft-nudity-detection and hard-nudity-detection, this model will
        only check for sensitive material that can be considered not-safe-for-work.

        ![AI Content Moderation: NSFW detection visual example](https://demo-files.gvideo.io/apidocs/nsfw-detection.gif)

        **How to use?**

        Frames within the specified video are analyzed.

        Response will contain only frames for which the class nsfw is detected with a
        confidence of more than 50%.

        Example of detected NSFW:

        ```
        {
          "nsfw_detected": true,
          "detection_results": [ "nsfw" ],
          "frames": [
              {
                  "label": "nsfw",
                  "confidence": 0.93,
                  "frame_number": 1
              },..
          ]
        }
        ```

        Example of a response without detecting inappropriate content:

        ```
        {
          "nsfw_detected": false,
          "detection_results": [],
          "frames": []
        }
        ```

        Please note that the API only provides a set of data (json) about the objects
        found, so no video is generated. The demo video video (above ^) was specially
        created based on json from the API for visual demonstration and better
        perception of the possibilities.

        Create AI CM:`hard_nudity` task

        This algorithm allows to detect explicit nudity of the human body (involving
        genitals) in a video. Generic info about all capabilities and limits see in the
        generic ["Content Moderation"](/api-reference/streaming/ai/create-ai-task)
        method.

        **What is Hard nudity detection?**

        This method is often used to analyze UGC to determine whether videos can be
        published to all users, or to prohibit publication due to offensive and
        inappropriate content.

        Objects that can be detected:

        - `ANUS_EXPOSED`
        - `BUTTOCKS_EXPOSED`
        - `FEMALE_BREAST_EXPOSED`
        - `FEMALE_GENITALIA_EXPOSED`
        - `MALE_BREAST_EXPOSED`
        - `MALE_GENITALIA_EXPOSED`

        Please note that the number of objects is less than in the
        soft-nudity-detection. This method works faster and better if only exposed body
        parts detection is required.

        ![AI Content Moderation: hard nudity detection visual example](https://demo-files.gvideo.io/apidocs/nudity_detection.gif)

        **How to use?**

        The information is returned with the video frame number where it was found and
        probability of the detected object. Nudity detection is done using AI, so for
        each object a probability percentage is applied; objects with a probability of
        at least 30% are included in the response.

        Video processing speed is approximately 1:5.

        Example of detected nudity or body parts:

        ```
        {
          "nudity_detected": true,
          "detection_results": [ "MALE_GENITALIA_EXPOSED" ]
          "frames": [
              {
                  "confidence": 0.75,
                  "frame_number": 35,
                  "label": "MALE_GENITALIA_EXPOSED"
              },...
          ]
        }
        ```

        Example response when nudity or body parts were not found:

        ```
        {
          "nudity_detected": false,
          "detection_results": []
          "frames": []
        }
        ```

        There is no universal recipe under which a video can be considered unacceptable,
        since different services host different types of videos for different audiences:
        adult content, children's content, educational content, etc. You can determine
        the probability threshold at which you consider a video inappropriate. The
        easiest option is to run several of your videos and analyze the resulting
        probability coefficient.

        Sometimes a detected object at the beginning of the video immediately makes it
        clear that there is no need to further analyze the video. For such cases, you
        can use stop tags. Use parameter "stop_objects" to specify comma separated stop
        tags. It is also possible to specify % probability threshold value, above which
        the stop tag will be triggered.

        ```
          {
              "url": "...",
              "stop_objects": "MALE_GENITALIA_EXPOSED:0.8,FEMALE_GENITALIA_EXPOSED"
          }
        ```

        Please note that the API only provides a set of data (json) about the objects
        found, so no video is generated. The demo video video (above ^) was specially
        created based on json from the API for visual demonstration and better
        perception of the possibilities.

        Create AI CM:`soft_nudity` task

        This algorithm allows to identify explicit nudity and partial nudity too
        (including the presence of male and female faces and other uncovered body parts)
        in a video. Generic info about all capabilities and limits see in the generic
        ["Content Moderation"](/api-reference/streaming/ai/create-ai-task) method.

        **What is Soft nudity detection?**

        This method is often used to analyze UGC to determine whether videos can be
        published to all users, or to prohibit publication due to offensive and
        inappropriate content.

        Objects that can be detected:

        - `ANUS_COVERED`
        - `ANUS_EXPOSED`
        - `ARMPITS_COVERED`
        - `ARMPITS_EXPOSED`
        - `BELLY_COVERED`
        - `BELLY_EXPOSED`
        - `BUTTOCKS_COVERED`
        - `BUTTOCKS_EXPOSED`
        - `FACE_FEMALE`
        - `FACE_MALE`
        - `FEET_COVERED`
        - `FEET_EXPOSED`
        - `FEMALE_BREAST_COVERED`
        - `FEMALE_BREAST_EXPOSED`
        - `FEMALE_GENITALIA_COVERED`
        - `FEMALE_GENITALIA_EXPOSED`
        - `MALE_BREAST_EXPOSED`
        - `MALE_GENITALIA_EXPOSED`

        This method allows you to identify faces and other body parts. Used to find
        complex combinations of what is happening in a video. Please note that the
        number of objects is more than in the hard-nudity-detection. The method is
        slower.

        ![AI Content Moderation: hard nudity detection visual example](https://demo-files.gvideo.io/apidocs/soft_nudity_detection.gif)

        **How to use?**

        The information is returned with the video frame number where it was found and
        probability of the detected object. Nudity detection is done using AI, so for
        each object a probability percentage is applied; objects with a probability of
        at least 30% are included in the response.

        Video processing speed is approximately 1:5.

        Example of detected nudity or body parts:

        ```
        {
          "nudity_detected": true,
          "detection_results": [ "FACE_FEMALE", "BELLY_COVERED" ]
          "frames": [
              {
                  "confidence": 0.82,
                  "frame_number": 1,
                  "label": "BELLY_COVERED"
              },...
          ]
        }
        ```

        Example response when nudity or body parts were not found:

        ```
        {
          "nudity_detected": false,
          "detection_results": []
          "frames": []
        }
        ```

        There is no universal recipe under which a video can be considered unacceptable,
        since different services host different types of videos for different audiences:
        adult content, children's content, educational content, etc. You can determine
        the probability threshold at which you consider a video inappropriate. The
        easiest option is to run several of your videos and analyze the resulting
        probability coefficient.

        Sometimes a detected object at the beginning of the video immediately makes it
        clear that there is no need to further analyze the video. For such cases, you
        can use stop tags. Use parameter "stop_objects" to specify comma separated stop
        tags. It is also possible to specify % probability threshold value, above which
        the stop tag will be triggered.

        ```
          {
              "url": "...",
              "stop_objects": "BELLY_COVERED:0.9,FEMALE_GENITALIA_COVERED"
          }
        ```

        Please note that the API only provides a set of data (json) about the objects
        found, so no video is generated. The demo video video (above ^) was specially
        created based on json from the API for visual demonstration and better
        perception of the possibilities.

        Create AI CM:sport task

        This algorithm allows to identify various sporting activities in a video.
        Generic info about all capabilities and limits see in the generic
        ["Content Moderation"](/api-reference/streaming/ai/create-ai-task) method.

        **What is Sports activity detection?**

        Sports activity detection by AI involves using machine learning and computer
        vision technologies to automatically identify, analyze, and interpret various
        activities within sports and generic videos. This can include detecting specific
        types, actions, events, and moments.

        This model operates on a video sequence (and not on images as most of the used
        computer vision models). Make sure your video is at least 10-15 seconds long.

        Sports activities can be detected:

        - archery
        - arm wrestling
        - playing badminton
        - playing baseball
        - basketball dunk
        - bowling
        - boxing punch
        - boxing speed bag
        - catching or throwing baseball
        - catching or throwing softball
        - cricket
        - curling
        - disc golfing
        - dodgeball
        - fencing
        - football
        - golf chipping
        - golf driving
        - golf putting
        - hitting baseball
        - hockey stop
        - ice skating
        - javelin throw
        - juggling soccer ball
        - kayaking
        - kicking field goal
        - kicking soccer ball
        - playing cricket
        - playing field hockey
        - playing ice hockey
        - playing kickball
        - playing lacrosse
        - playing ping pong
        - playing polo
        - playing squash or racquetball
        - playing tennis
        - playing volleyball
        - pole vault
        - riding a bike
        - riding or walking with horse
        - roller skating
        - rowing
        - sailing
        - shooting goal (soccer)
        - skateboarding
        - skiing

        Use cases:

        - Sports leagues and content creators can use AI to monitor UGC for unauthorized
          publications of their content. This can include detecting specific sporting
          events or activities that are part of copyrighted content.
        - Sports fans often miss live games and rely on highlight reels. AI can
          automatically detect key moments like goals, touchdowns, or game-winning shots
          in uploaded UGC videos and compile them into personalized highlight reels.

        ![AI Content Moderation: sports activity detection visual example](https://demo-files.gvideo.io/apidocs/sports_football_detection.gif)

        **How to use?**

        The information is returned with the video frame number where it was found and
        probability of the detected activity. Identification is done using AI, so for
        each activity a probability percentage is applied; activities with a probability
        of at least 30% are included in the response.

        Video processing speed is approximately 1:5.

        Example of detected sports activity:

        ```
        {
          "sport_detected": true,
          "detection_results": [ "shooting goal (soccer)" ],
          "frames": [
              {
                  "label": "shooting goal (soccer)",
                  "frame_number": 98,
                  "confidence": 0.99
              },...
          ]
        }
        ```

        Example response when sports activities were not found:

        ```
        {
          "sport_detected": false,
          "detection_results": []
          "frames": []
        }
        ```

        Please note that the API only provides a set of data (json) about the objects
        found, so no video is generated. The demo video video (above ^) was specially
        created based on json from the API for visual demonstration and better
        perception of the possibilities.

        Args:
          task_name: Name of the task to be performed

          url: URL to the MP4 file to analyze. File must be publicly accessible via HTTP/HTTPS.

          audio_language: Language in original audio (transcription only). This value is used to determine
              the language from which to transcribe.

              If this is not set, the system will run auto language identification and the
              subtitles will be in the detected language. The method also works based on AI
              analysis. It's fairly accurate, but if it's wrong, then set the language
              explicitly.

              Additionally, when this is not set, we also support recognition of alternate
              languages in the video (language code-switching).

              Language is set by 3-letter language code according to ISO-639-2 (bibliographic
              code).

              We can process languages:

              - 'afr': Afrikaans
              - 'alb': Albanian
              - 'amh': Amharic
              - 'ara': Arabic
              - 'arm': Armenian
              - 'asm': Assamese
              - 'aze': Azerbaijani
              - 'bak': Bashkir
              - 'baq': Basque
              - 'bel': Belarusian
              - 'ben': Bengali
              - 'bos': Bosnian
              - 'bre': Breton
              - 'bul': Bulgarian
              - 'bur': Myanmar
              - 'cat': Catalan
              - 'chi': Chinese
              - 'cze': Czech
              - 'dan': Danish
              - 'dut': Nynorsk
              - 'eng': English
              - 'est': Estonian
              - 'fao': Faroese
              - 'fin': Finnish
              - 'fre': French
              - 'geo': Georgian
              - 'ger': German
              - 'glg': Galician
              - 'gre': Greek
              - 'guj': Gujarati
              - 'hat': Haitian creole
              - 'hau': Hausa
              - 'haw': Hawaiian
              - 'heb': Hebrew
              - 'hin': Hindi
              - 'hrv': Croatian
              - 'hun': Hungarian
              - 'ice': Icelandic
              - 'ind': Indonesian
              - 'ita': Italian
              - 'jav': Javanese
              - 'jpn': Japanese
              - 'kan': Kannada
              - 'kaz': Kazakh
              - 'khm': Khmer
              - 'kor': Korean
              - 'lao': Lao
              - 'lat': Latin
              - 'lav': Latvian
              - 'lin': Lingala
              - 'lit': Lithuanian
              - 'ltz': Luxembourgish
              - 'mac': Macedonian
              - 'mal': Malayalam
              - 'mao': Maori
              - 'mar': Marathi
              - 'may': Malay
              - 'mlg': Malagasy
              - 'mlt': Maltese
              - 'mon': Mongolian
              - 'nep': Nepali
              - 'dut': Dutch
              - 'nor': Norwegian
              - 'oci': Occitan
              - 'pan': Punjabi
              - 'per': Persian
              - 'pol': Polish
              - 'por': Portuguese
              - 'pus': Pashto
              - 'rum': Romanian
              - 'rus': Russian
              - 'san': Sanskrit
              - 'sin': Sinhala
              - 'slo': Slovak
              - 'slv': Slovenian
              - 'sna': Shona
              - 'snd': Sindhi
              - 'som': Somali
              - 'spa': Spanish
              - 'srp': Serbian
              - 'sun': Sundanese
              - 'swa': Swahili
              - 'swe': Swedish
              - 'tam': Tamil
              - 'tat': Tatar
              - 'tel': Telugu
              - 'tgk': Tajik
              - 'tgl': Tagalog
              - 'tha': Thai
              - 'tib': Tibetan
              - 'tuk': Turkmen
              - 'tur': Turkish
              - 'ukr': Ukrainian
              - 'urd': Urdu
              - 'uzb': Uzbek
              - 'vie': Vietnamese
              - 'wel': Welsh
              - 'yid': Yiddish
              - 'yor': Yoruba

          client_entity_data: Meta parameter, designed to store your own extra information about a video
              entity: video source, video id, etc. It is not used in any way in video
              processing.

              For example, if an AI-task was created automatically when you uploaded a video
              with the AI auto-processing option (transcribing, translation), then the ID of
              the associated video for which the task was performed will be explicitly
              indicated here.

          client_user_id: Meta parameter, designed to store your own identifier. Can be used by you to tag
              requests from different end-users. It is not used in any way in video
              processing.

          subtitles_language: Indicates which language it is clearly necessary to translate into. If this is
              not set, the original language will be used from attribute "audio_language".

              Please note that:

              - transcription into the original language is a free procedure,
              - and translation from the original language into any other languages is a
                "translation" procedure and is paid. More details in
                [POST /streaming/ai/tasks](/api-reference/streaming/ai/create-ai-task).
                Language is set by 3-letter language code according to ISO-639-2
                (bibliographic code).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        category: Literal["nsfw"],
        task_name: Literal["content-moderation"],
        url: str,
        client_entity_data: str | Omit = omit,
        client_user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AITaskCreateResponse:
        """
        Creating an AI task.

        This method allows you to create an AI task for VOD video processing:

        - ASR: Transcribe video
        - ASR: Translate subtitles
        - CM: Sports detection
        - CM: Not Safe For Work (NSFW) content detection
        - CM: Soft nudity detection
        - CM: Hard nudity detection
        - CM: Objects recognition (soon)

        ![Auto generated subtitles example](https://demo-files.gvideo.io/apidocs/captions.gif)

        How to use:

        - Create an AI task, specify algorithm to use
        - Get `task_id`
        - Check a result using `.../ai/tasks/{task_id}` method

        For more detailed information, see the algorithm-specific sections below.

        **AI Automatic Speech Recognition (ASR)**

        AI is instrumental in automatic video processing for subtitles creation by using
        Automatic Speech Recognition (ASR) technology to transcribe spoken words into
        text, which can then be translated into multiple languages for broader
        accessibility.

        Categories:

        - `transcription` – to create subtitles/captions from audio in the original
          language.
        - `translation` – to translate subtitles/captions from the original language to
          99+ other languages.

        AI subtitle transcription and translation tools are highly efficient, processing
        large volumes of audio-visual content quickly and providing accurate
        transcriptions and translations with minimal human intervention. Additionally,
        AI-driven solutions can significantly reduce costs and turnaround times compared
        to traditional methods, making them an invaluable resource for content creators
        and broadcasters aiming to reach global audiences.

        Example response with positive result:

        ```
        {
          "status": "SUCCESS",
          "result": {
            "subtitles": [
              {
                  "start_time": "00:00:00.031",
                  "end_time": "00:00:03.831",
                  "text": "Come on team, ..."
              }, ...
            ]
            "vttContent": "WEBVTT\n\n1\n00:00:00.031 --> 00:00:03.831\nCome on team, ...",
            "concatenated_text": "Come on team, ...",
            "languages": [ "eng" ],
            "speech_detected": true
            }
          }, ...
        }
        ```

        **AI Content Moderation (CM)**

        The AI Content Moderation API offers a powerful solution for analyzing video
        content to detect various categories of inappropriate material. Leveraging
        state-of-the-art AI models, this API ensures real-time analysis and flagging of
        sensitive or restricted content types, making it an essential tool for platforms
        requiring stringent content moderation.

        Categories:

        - `nsfw`: Quick algorithm to detect pornographic material, ensuring content is
          "not-safe-for-work" or normal.
        - `hard_nudity`: Detailed analysis of video which detects explicit nudity
          involving genitalia.
        - `soft_nudity`: Detailed video analysis that reveals both explicit and partial
          nudity, including the presence of male and female faces and other uncovered
          body parts.
        - `sport`: Recognizes various sporting activities.

        The AI Content Moderation API is an invaluable tool for managing and controlling
        the type of content being shared or streamed on your platform. By implementing
        this API, you can ensure compliance with community guidelines and legal
        requirements, as well as provide a safer environment for your users.

        Important notes:

        - It's allowed to analyze still images too (where applicable). Format of image:
          JPEG, PNG. In that case one image is the same as video of 1 second duration.
        - Not all frames in the video are used for analysis, but only key frames
          (Iframe). For example, if a key frame in a video is set every ±2 seconds, then
          detection will only occur at these timestamps. If an object appears and
          disappears between these time stamps, it will not be detected. We are working
          on a version to analyze more frames, please contact your manager or our
          support team to enable this method.

        Example response with positive result:

        ```
        {
          "status": "SUCCESS",
          "result": {
              "nsfw_detected": true,
              "detection_results": [ "nsfw" ],
              "frames": [
                  {
                      "label": "nsfw",
                      "confidence": 1.0,
                      "frame_number": 24
                  },...
              ]
          }
        }
        ```

        **Additional information**

        Billing takes into account the duration of the analyzed video. Or the duration
        until the stop tag(where applicable), if the condition was triggered during the
        analysis.

        The heart of content moderation is AI, with additional services. They run on our
        own infrastructure, so the files/data are not transferred anywhere to external
        services. After processing, original files are also deleted from local storage
        of AI.

        Read more detailed information about our solution, and architecture, and
        benefits in the knowledge base and blog.

        **Algorithm-specific details**

        Create AI ASR task

        Transcribing is the process of writing down the words you hear in an audio. Our
        solution allows you to transcribe audio from your video and get subtitles
        automatically. To do this, we use modern AI models.

        The result:

        - Transcription – subtitles in the original language. I.e. audio is in English –
          subtitles are in English too, audio is in German – subtitles are in German
          too.
        - Translation – subtitles is translated from the original language to any other
          language.

        **How to use?**

        - Explicit call to this AI method. Applicable for any file stored with us or
          located on the Internet.
        - Standard video upload but with automatic subtitle generation. Look at
          ["VOD uploading"](/api-reference/streaming/videos/create-video).

        **What language will the subtitles be in?**

        You can specify the language explicitly, then it will be used to create
        subtitles: the source language in the audio, the resulting subtitle language. If
        this is not set, the system will run auto language identification and the
        subtitles will be in the detected language. The method also works based on AI
        analysis.

        Additionally, when this is not set, we also support recognition of alternate
        languages in the video (code-switching). For example, when in a video different
        speakers speak several languages, or when they switch from their native language
        to English and back. Thus when you have multiple languages in the video it is
        better to not specify an "audio_language" otherwise AI may force the system to
        recognize gibberish.

        **What can be transcribed?**

        Service uses additional methods to detect presence of speech in audio track,
        thus improving the detection of any human conversations:

        - Speech of one speaker,
        - Speech of several speakers,
        - Speech in different languages,
        - etc

        Restriction on music, lyrics most likely will not be created.

        **What about translation?**

        It is also possible to automatically translate from the original language to
        another you need.

        To create a translation, specify the desired language explicitly in
        "subtitles_language" parameter. Otherwise, the subtitles will be in the original
        language. Translation into different languages should be done by creating
        separate tasks.

        ![Auto generated subtitles example](https://demo-files.gvideo.io/apidocs/captions.gif)

        Use MP4 videos to process. This method is not tied to videos that are stored
        only in our video hosting (look at how get a link to MP4 rendition), so you can
        use links to any other external file with HTTP/HTTPS access.

        For now, only the first audio track can be processed; later this functionality
        will be improved to allow to use any. Also, not all language pairs are currently
        supported. If a language pair is not supported for automatic translation, the
        task status will be FAILURE with description of the reason. Example:
        `eng => uzb`. You can request to add the language pair you need for automatic
        translation. Contact our support.

        Example of modes to transcribe and/or translate:

        - Auto language detection: `{ "url":"..." }`
        - From German language explicitly : `{ "url":"...", "audio_language":"ger" }`
        - From any auto-detected to English language explicitly:
          `{ "url":"...", "subtitles_language":"eng" }`
        - From German language to English language explicitly:
          `{ "url":"...", "audio_language":"ger", "subtitles_language":"eng" }`

        Example of setting a task to process MP4 file (animated gif from above):

        ```
        curl -L 'https://api.gcore.com/streaming/ai/tasks' \\
        -H 'Content-Type: application/json' \\
        -H 'Authorization: APIKey 1234$abcd...' \\
        -d '{
            "url": "https://demo-files.gvideo.io/apidocs/spritefright-blender-cut30sec.mp4"
        }'
        ```

        As described above, transcription is done automatically using AI. Therefore, the
        quality may differ from a manual transcription by a professional person. If this
        happens to you, then you can download subtitles and change them in an external
        editor.

        Transcription and translation are 2 different AI tasks:

        - Transcription is set only for transcription.
        - Translation, if non-original languages are set for translation.

        Billing takes into account the duration of the analyzed original video.

        The heart for transcribing is the AI model Whisper from OpenAI, with additional
        optimizations and services. The AI models run on our own infrastructure, so the
        files/data are not transferred anywhere to external services. After processing,
        original files are also deleted from local storage of AI.

        Read more detailed information about our solution, and architecture, and
        benefits in the knowledge base and blog.

        Create AI CM:nsfw task

        This algorithm allows to quickly detect inappropriate content, determining that
        the content is NSFW ("Not Safe For Work") or normal. Generic info about all
        capabilities and limits see in the generic
        ["Content Moderation"](/api-reference/streaming/ai/create-ai-task) method.

        **What is "Not Safe For Work"?**

        The algorithm has recognized inappropriate content in a video and it might not
        be suitable to view in public places. The solution provides its confidence level
        (in percentage) of how sure it is that the content is NSFW, or it most likely
        does not contain any sexual or similar content.

        Different to soft-nudity-detection and hard-nudity-detection, this model will
        only check for sensitive material that can be considered not-safe-for-work.

        ![AI Content Moderation: NSFW detection visual example](https://demo-files.gvideo.io/apidocs/nsfw-detection.gif)

        **How to use?**

        Frames within the specified video are analyzed.

        Response will contain only frames for which the class nsfw is detected with a
        confidence of more than 50%.

        Example of detected NSFW:

        ```
        {
          "nsfw_detected": true,
          "detection_results": [ "nsfw" ],
          "frames": [
              {
                  "label": "nsfw",
                  "confidence": 0.93,
                  "frame_number": 1
              },..
          ]
        }
        ```

        Example of a response without detecting inappropriate content:

        ```
        {
          "nsfw_detected": false,
          "detection_results": [],
          "frames": []
        }
        ```

        Please note that the API only provides a set of data (json) about the objects
        found, so no video is generated. The demo video video (above ^) was specially
        created based on json from the API for visual demonstration and better
        perception of the possibilities.

        Create AI CM:`hard_nudity` task

        This algorithm allows to detect explicit nudity of the human body (involving
        genitals) in a video. Generic info about all capabilities and limits see in the
        generic ["Content Moderation"](/api-reference/streaming/ai/create-ai-task)
        method.

        **What is Hard nudity detection?**

        This method is often used to analyze UGC to determine whether videos can be
        published to all users, or to prohibit publication due to offensive and
        inappropriate content.

        Objects that can be detected:

        - `ANUS_EXPOSED`
        - `BUTTOCKS_EXPOSED`
        - `FEMALE_BREAST_EXPOSED`
        - `FEMALE_GENITALIA_EXPOSED`
        - `MALE_BREAST_EXPOSED`
        - `MALE_GENITALIA_EXPOSED`

        Please note that the number of objects is less than in the
        soft-nudity-detection. This method works faster and better if only exposed body
        parts detection is required.

        ![AI Content Moderation: hard nudity detection visual example](https://demo-files.gvideo.io/apidocs/nudity_detection.gif)

        **How to use?**

        The information is returned with the video frame number where it was found and
        probability of the detected object. Nudity detection is done using AI, so for
        each object a probability percentage is applied; objects with a probability of
        at least 30% are included in the response.

        Video processing speed is approximately 1:5.

        Example of detected nudity or body parts:

        ```
        {
          "nudity_detected": true,
          "detection_results": [ "MALE_GENITALIA_EXPOSED" ]
          "frames": [
              {
                  "confidence": 0.75,
                  "frame_number": 35,
                  "label": "MALE_GENITALIA_EXPOSED"
              },...
          ]
        }
        ```

        Example response when nudity or body parts were not found:

        ```
        {
          "nudity_detected": false,
          "detection_results": []
          "frames": []
        }
        ```

        There is no universal recipe under which a video can be considered unacceptable,
        since different services host different types of videos for different audiences:
        adult content, children's content, educational content, etc. You can determine
        the probability threshold at which you consider a video inappropriate. The
        easiest option is to run several of your videos and analyze the resulting
        probability coefficient.

        Sometimes a detected object at the beginning of the video immediately makes it
        clear that there is no need to further analyze the video. For such cases, you
        can use stop tags. Use parameter "stop_objects" to specify comma separated stop
        tags. It is also possible to specify % probability threshold value, above which
        the stop tag will be triggered.

        ```
          {
              "url": "...",
              "stop_objects": "MALE_GENITALIA_EXPOSED:0.8,FEMALE_GENITALIA_EXPOSED"
          }
        ```

        Please note that the API only provides a set of data (json) about the objects
        found, so no video is generated. The demo video video (above ^) was specially
        created based on json from the API for visual demonstration and better
        perception of the possibilities.

        Create AI CM:`soft_nudity` task

        This algorithm allows to identify explicit nudity and partial nudity too
        (including the presence of male and female faces and other uncovered body parts)
        in a video. Generic info about all capabilities and limits see in the generic
        ["Content Moderation"](/api-reference/streaming/ai/create-ai-task) method.

        **What is Soft nudity detection?**

        This method is often used to analyze UGC to determine whether videos can be
        published to all users, or to prohibit publication due to offensive and
        inappropriate content.

        Objects that can be detected:

        - `ANUS_COVERED`
        - `ANUS_EXPOSED`
        - `ARMPITS_COVERED`
        - `ARMPITS_EXPOSED`
        - `BELLY_COVERED`
        - `BELLY_EXPOSED`
        - `BUTTOCKS_COVERED`
        - `BUTTOCKS_EXPOSED`
        - `FACE_FEMALE`
        - `FACE_MALE`
        - `FEET_COVERED`
        - `FEET_EXPOSED`
        - `FEMALE_BREAST_COVERED`
        - `FEMALE_BREAST_EXPOSED`
        - `FEMALE_GENITALIA_COVERED`
        - `FEMALE_GENITALIA_EXPOSED`
        - `MALE_BREAST_EXPOSED`
        - `MALE_GENITALIA_EXPOSED`

        This method allows you to identify faces and other body parts. Used to find
        complex combinations of what is happening in a video. Please note that the
        number of objects is more than in the hard-nudity-detection. The method is
        slower.

        ![AI Content Moderation: hard nudity detection visual example](https://demo-files.gvideo.io/apidocs/soft_nudity_detection.gif)

        **How to use?**

        The information is returned with the video frame number where it was found and
        probability of the detected object. Nudity detection is done using AI, so for
        each object a probability percentage is applied; objects with a probability of
        at least 30% are included in the response.

        Video processing speed is approximately 1:5.

        Example of detected nudity or body parts:

        ```
        {
          "nudity_detected": true,
          "detection_results": [ "FACE_FEMALE", "BELLY_COVERED" ]
          "frames": [
              {
                  "confidence": 0.82,
                  "frame_number": 1,
                  "label": "BELLY_COVERED"
              },...
          ]
        }
        ```

        Example response when nudity or body parts were not found:

        ```
        {
          "nudity_detected": false,
          "detection_results": []
          "frames": []
        }
        ```

        There is no universal recipe under which a video can be considered unacceptable,
        since different services host different types of videos for different audiences:
        adult content, children's content, educational content, etc. You can determine
        the probability threshold at which you consider a video inappropriate. The
        easiest option is to run several of your videos and analyze the resulting
        probability coefficient.

        Sometimes a detected object at the beginning of the video immediately makes it
        clear that there is no need to further analyze the video. For such cases, you
        can use stop tags. Use parameter "stop_objects" to specify comma separated stop
        tags. It is also possible to specify % probability threshold value, above which
        the stop tag will be triggered.

        ```
          {
              "url": "...",
              "stop_objects": "BELLY_COVERED:0.9,FEMALE_GENITALIA_COVERED"
          }
        ```

        Please note that the API only provides a set of data (json) about the objects
        found, so no video is generated. The demo video video (above ^) was specially
        created based on json from the API for visual demonstration and better
        perception of the possibilities.

        Create AI CM:sport task

        This algorithm allows to identify various sporting activities in a video.
        Generic info about all capabilities and limits see in the generic
        ["Content Moderation"](/api-reference/streaming/ai/create-ai-task) method.

        **What is Sports activity detection?**

        Sports activity detection by AI involves using machine learning and computer
        vision technologies to automatically identify, analyze, and interpret various
        activities within sports and generic videos. This can include detecting specific
        types, actions, events, and moments.

        This model operates on a video sequence (and not on images as most of the used
        computer vision models). Make sure your video is at least 10-15 seconds long.

        Sports activities can be detected:

        - archery
        - arm wrestling
        - playing badminton
        - playing baseball
        - basketball dunk
        - bowling
        - boxing punch
        - boxing speed bag
        - catching or throwing baseball
        - catching or throwing softball
        - cricket
        - curling
        - disc golfing
        - dodgeball
        - fencing
        - football
        - golf chipping
        - golf driving
        - golf putting
        - hitting baseball
        - hockey stop
        - ice skating
        - javelin throw
        - juggling soccer ball
        - kayaking
        - kicking field goal
        - kicking soccer ball
        - playing cricket
        - playing field hockey
        - playing ice hockey
        - playing kickball
        - playing lacrosse
        - playing ping pong
        - playing polo
        - playing squash or racquetball
        - playing tennis
        - playing volleyball
        - pole vault
        - riding a bike
        - riding or walking with horse
        - roller skating
        - rowing
        - sailing
        - shooting goal (soccer)
        - skateboarding
        - skiing

        Use cases:

        - Sports leagues and content creators can use AI to monitor UGC for unauthorized
          publications of their content. This can include detecting specific sporting
          events or activities that are part of copyrighted content.
        - Sports fans often miss live games and rely on highlight reels. AI can
          automatically detect key moments like goals, touchdowns, or game-winning shots
          in uploaded UGC videos and compile them into personalized highlight reels.

        ![AI Content Moderation: sports activity detection visual example](https://demo-files.gvideo.io/apidocs/sports_football_detection.gif)

        **How to use?**

        The information is returned with the video frame number where it was found and
        probability of the detected activity. Identification is done using AI, so for
        each activity a probability percentage is applied; activities with a probability
        of at least 30% are included in the response.

        Video processing speed is approximately 1:5.

        Example of detected sports activity:

        ```
        {
          "sport_detected": true,
          "detection_results": [ "shooting goal (soccer)" ],
          "frames": [
              {
                  "label": "shooting goal (soccer)",
                  "frame_number": 98,
                  "confidence": 0.99
              },...
          ]
        }
        ```

        Example response when sports activities were not found:

        ```
        {
          "sport_detected": false,
          "detection_results": []
          "frames": []
        }
        ```

        Please note that the API only provides a set of data (json) about the objects
        found, so no video is generated. The demo video video (above ^) was specially
        created based on json from the API for visual demonstration and better
        perception of the possibilities.

        Args:
          category: AI content moderation with NSFW detection algorithm

          task_name: Name of the task to be performed

          url: URL to the MP4 file to analyze. File must be publicly accessible via HTTP/HTTPS.

          client_entity_data: Meta parameter, designed to store your own extra information about a video
              entity: video source, video id, etc. It is not used in any way in video
              processing.

              For example, if an AI-task was created automatically when you uploaded a video
              with the AI auto-processing option (nudity detection, etc), then the ID of the
              associated video for which the task was performed will be explicitly indicated
              here.

          client_user_id: Meta parameter, designed to store your own identifier. Can be used by you to tag
              requests from different end-users. It is not used in any way in video
              processing.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        category: Literal["hard_nudity"],
        task_name: Literal["content-moderation"],
        url: str,
        client_entity_data: str | Omit = omit,
        client_user_id: str | Omit = omit,
        stop_objects: Literal[
            "ANUS_EXPOSED",
            "BUTTOCKS_EXPOSED",
            "FEMALE_BREAST_EXPOSED",
            "FEMALE_GENITALIA_EXPOSED",
            "MALE_BREAST_EXPOSED",
            "MALE_GENITALIA_EXPOSED",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AITaskCreateResponse:
        """
        Creating an AI task.

        This method allows you to create an AI task for VOD video processing:

        - ASR: Transcribe video
        - ASR: Translate subtitles
        - CM: Sports detection
        - CM: Not Safe For Work (NSFW) content detection
        - CM: Soft nudity detection
        - CM: Hard nudity detection
        - CM: Objects recognition (soon)

        ![Auto generated subtitles example](https://demo-files.gvideo.io/apidocs/captions.gif)

        How to use:

        - Create an AI task, specify algorithm to use
        - Get `task_id`
        - Check a result using `.../ai/tasks/{task_id}` method

        For more detailed information, see the algorithm-specific sections below.

        **AI Automatic Speech Recognition (ASR)**

        AI is instrumental in automatic video processing for subtitles creation by using
        Automatic Speech Recognition (ASR) technology to transcribe spoken words into
        text, which can then be translated into multiple languages for broader
        accessibility.

        Categories:

        - `transcription` – to create subtitles/captions from audio in the original
          language.
        - `translation` – to translate subtitles/captions from the original language to
          99+ other languages.

        AI subtitle transcription and translation tools are highly efficient, processing
        large volumes of audio-visual content quickly and providing accurate
        transcriptions and translations with minimal human intervention. Additionally,
        AI-driven solutions can significantly reduce costs and turnaround times compared
        to traditional methods, making them an invaluable resource for content creators
        and broadcasters aiming to reach global audiences.

        Example response with positive result:

        ```
        {
          "status": "SUCCESS",
          "result": {
            "subtitles": [
              {
                  "start_time": "00:00:00.031",
                  "end_time": "00:00:03.831",
                  "text": "Come on team, ..."
              }, ...
            ]
            "vttContent": "WEBVTT\n\n1\n00:00:00.031 --> 00:00:03.831\nCome on team, ...",
            "concatenated_text": "Come on team, ...",
            "languages": [ "eng" ],
            "speech_detected": true
            }
          }, ...
        }
        ```

        **AI Content Moderation (CM)**

        The AI Content Moderation API offers a powerful solution for analyzing video
        content to detect various categories of inappropriate material. Leveraging
        state-of-the-art AI models, this API ensures real-time analysis and flagging of
        sensitive or restricted content types, making it an essential tool for platforms
        requiring stringent content moderation.

        Categories:

        - `nsfw`: Quick algorithm to detect pornographic material, ensuring content is
          "not-safe-for-work" or normal.
        - `hard_nudity`: Detailed analysis of video which detects explicit nudity
          involving genitalia.
        - `soft_nudity`: Detailed video analysis that reveals both explicit and partial
          nudity, including the presence of male and female faces and other uncovered
          body parts.
        - `sport`: Recognizes various sporting activities.

        The AI Content Moderation API is an invaluable tool for managing and controlling
        the type of content being shared or streamed on your platform. By implementing
        this API, you can ensure compliance with community guidelines and legal
        requirements, as well as provide a safer environment for your users.

        Important notes:

        - It's allowed to analyze still images too (where applicable). Format of image:
          JPEG, PNG. In that case one image is the same as video of 1 second duration.
        - Not all frames in the video are used for analysis, but only key frames
          (Iframe). For example, if a key frame in a video is set every ±2 seconds, then
          detection will only occur at these timestamps. If an object appears and
          disappears between these time stamps, it will not be detected. We are working
          on a version to analyze more frames, please contact your manager or our
          support team to enable this method.

        Example response with positive result:

        ```
        {
          "status": "SUCCESS",
          "result": {
              "nsfw_detected": true,
              "detection_results": [ "nsfw" ],
              "frames": [
                  {
                      "label": "nsfw",
                      "confidence": 1.0,
                      "frame_number": 24
                  },...
              ]
          }
        }
        ```

        **Additional information**

        Billing takes into account the duration of the analyzed video. Or the duration
        until the stop tag(where applicable), if the condition was triggered during the
        analysis.

        The heart of content moderation is AI, with additional services. They run on our
        own infrastructure, so the files/data are not transferred anywhere to external
        services. After processing, original files are also deleted from local storage
        of AI.

        Read more detailed information about our solution, and architecture, and
        benefits in the knowledge base and blog.

        **Algorithm-specific details**

        Create AI ASR task

        Transcribing is the process of writing down the words you hear in an audio. Our
        solution allows you to transcribe audio from your video and get subtitles
        automatically. To do this, we use modern AI models.

        The result:

        - Transcription – subtitles in the original language. I.e. audio is in English –
          subtitles are in English too, audio is in German – subtitles are in German
          too.
        - Translation – subtitles is translated from the original language to any other
          language.

        **How to use?**

        - Explicit call to this AI method. Applicable for any file stored with us or
          located on the Internet.
        - Standard video upload but with automatic subtitle generation. Look at
          ["VOD uploading"](/api-reference/streaming/videos/create-video).

        **What language will the subtitles be in?**

        You can specify the language explicitly, then it will be used to create
        subtitles: the source language in the audio, the resulting subtitle language. If
        this is not set, the system will run auto language identification and the
        subtitles will be in the detected language. The method also works based on AI
        analysis.

        Additionally, when this is not set, we also support recognition of alternate
        languages in the video (code-switching). For example, when in a video different
        speakers speak several languages, or when they switch from their native language
        to English and back. Thus when you have multiple languages in the video it is
        better to not specify an "audio_language" otherwise AI may force the system to
        recognize gibberish.

        **What can be transcribed?**

        Service uses additional methods to detect presence of speech in audio track,
        thus improving the detection of any human conversations:

        - Speech of one speaker,
        - Speech of several speakers,
        - Speech in different languages,
        - etc

        Restriction on music, lyrics most likely will not be created.

        **What about translation?**

        It is also possible to automatically translate from the original language to
        another you need.

        To create a translation, specify the desired language explicitly in
        "subtitles_language" parameter. Otherwise, the subtitles will be in the original
        language. Translation into different languages should be done by creating
        separate tasks.

        ![Auto generated subtitles example](https://demo-files.gvideo.io/apidocs/captions.gif)

        Use MP4 videos to process. This method is not tied to videos that are stored
        only in our video hosting (look at how get a link to MP4 rendition), so you can
        use links to any other external file with HTTP/HTTPS access.

        For now, only the first audio track can be processed; later this functionality
        will be improved to allow to use any. Also, not all language pairs are currently
        supported. If a language pair is not supported for automatic translation, the
        task status will be FAILURE with description of the reason. Example:
        `eng => uzb`. You can request to add the language pair you need for automatic
        translation. Contact our support.

        Example of modes to transcribe and/or translate:

        - Auto language detection: `{ "url":"..." }`
        - From German language explicitly : `{ "url":"...", "audio_language":"ger" }`
        - From any auto-detected to English language explicitly:
          `{ "url":"...", "subtitles_language":"eng" }`
        - From German language to English language explicitly:
          `{ "url":"...", "audio_language":"ger", "subtitles_language":"eng" }`

        Example of setting a task to process MP4 file (animated gif from above):

        ```
        curl -L 'https://api.gcore.com/streaming/ai/tasks' \\
        -H 'Content-Type: application/json' \\
        -H 'Authorization: APIKey 1234$abcd...' \\
        -d '{
            "url": "https://demo-files.gvideo.io/apidocs/spritefright-blender-cut30sec.mp4"
        }'
        ```

        As described above, transcription is done automatically using AI. Therefore, the
        quality may differ from a manual transcription by a professional person. If this
        happens to you, then you can download subtitles and change them in an external
        editor.

        Transcription and translation are 2 different AI tasks:

        - Transcription is set only for transcription.
        - Translation, if non-original languages are set for translation.

        Billing takes into account the duration of the analyzed original video.

        The heart for transcribing is the AI model Whisper from OpenAI, with additional
        optimizations and services. The AI models run on our own infrastructure, so the
        files/data are not transferred anywhere to external services. After processing,
        original files are also deleted from local storage of AI.

        Read more detailed information about our solution, and architecture, and
        benefits in the knowledge base and blog.

        Create AI CM:nsfw task

        This algorithm allows to quickly detect inappropriate content, determining that
        the content is NSFW ("Not Safe For Work") or normal. Generic info about all
        capabilities and limits see in the generic
        ["Content Moderation"](/api-reference/streaming/ai/create-ai-task) method.

        **What is "Not Safe For Work"?**

        The algorithm has recognized inappropriate content in a video and it might not
        be suitable to view in public places. The solution provides its confidence level
        (in percentage) of how sure it is that the content is NSFW, or it most likely
        does not contain any sexual or similar content.

        Different to soft-nudity-detection and hard-nudity-detection, this model will
        only check for sensitive material that can be considered not-safe-for-work.

        ![AI Content Moderation: NSFW detection visual example](https://demo-files.gvideo.io/apidocs/nsfw-detection.gif)

        **How to use?**

        Frames within the specified video are analyzed.

        Response will contain only frames for which the class nsfw is detected with a
        confidence of more than 50%.

        Example of detected NSFW:

        ```
        {
          "nsfw_detected": true,
          "detection_results": [ "nsfw" ],
          "frames": [
              {
                  "label": "nsfw",
                  "confidence": 0.93,
                  "frame_number": 1
              },..
          ]
        }
        ```

        Example of a response without detecting inappropriate content:

        ```
        {
          "nsfw_detected": false,
          "detection_results": [],
          "frames": []
        }
        ```

        Please note that the API only provides a set of data (json) about the objects
        found, so no video is generated. The demo video video (above ^) was specially
        created based on json from the API for visual demonstration and better
        perception of the possibilities.

        Create AI CM:`hard_nudity` task

        This algorithm allows to detect explicit nudity of the human body (involving
        genitals) in a video. Generic info about all capabilities and limits see in the
        generic ["Content Moderation"](/api-reference/streaming/ai/create-ai-task)
        method.

        **What is Hard nudity detection?**

        This method is often used to analyze UGC to determine whether videos can be
        published to all users, or to prohibit publication due to offensive and
        inappropriate content.

        Objects that can be detected:

        - `ANUS_EXPOSED`
        - `BUTTOCKS_EXPOSED`
        - `FEMALE_BREAST_EXPOSED`
        - `FEMALE_GENITALIA_EXPOSED`
        - `MALE_BREAST_EXPOSED`
        - `MALE_GENITALIA_EXPOSED`

        Please note that the number of objects is less than in the
        soft-nudity-detection. This method works faster and better if only exposed body
        parts detection is required.

        ![AI Content Moderation: hard nudity detection visual example](https://demo-files.gvideo.io/apidocs/nudity_detection.gif)

        **How to use?**

        The information is returned with the video frame number where it was found and
        probability of the detected object. Nudity detection is done using AI, so for
        each object a probability percentage is applied; objects with a probability of
        at least 30% are included in the response.

        Video processing speed is approximately 1:5.

        Example of detected nudity or body parts:

        ```
        {
          "nudity_detected": true,
          "detection_results": [ "MALE_GENITALIA_EXPOSED" ]
          "frames": [
              {
                  "confidence": 0.75,
                  "frame_number": 35,
                  "label": "MALE_GENITALIA_EXPOSED"
              },...
          ]
        }
        ```

        Example response when nudity or body parts were not found:

        ```
        {
          "nudity_detected": false,
          "detection_results": []
          "frames": []
        }
        ```

        There is no universal recipe under which a video can be considered unacceptable,
        since different services host different types of videos for different audiences:
        adult content, children's content, educational content, etc. You can determine
        the probability threshold at which you consider a video inappropriate. The
        easiest option is to run several of your videos and analyze the resulting
        probability coefficient.

        Sometimes a detected object at the beginning of the video immediately makes it
        clear that there is no need to further analyze the video. For such cases, you
        can use stop tags. Use parameter "stop_objects" to specify comma separated stop
        tags. It is also possible to specify % probability threshold value, above which
        the stop tag will be triggered.

        ```
          {
              "url": "...",
              "stop_objects": "MALE_GENITALIA_EXPOSED:0.8,FEMALE_GENITALIA_EXPOSED"
          }
        ```

        Please note that the API only provides a set of data (json) about the objects
        found, so no video is generated. The demo video video (above ^) was specially
        created based on json from the API for visual demonstration and better
        perception of the possibilities.

        Create AI CM:`soft_nudity` task

        This algorithm allows to identify explicit nudity and partial nudity too
        (including the presence of male and female faces and other uncovered body parts)
        in a video. Generic info about all capabilities and limits see in the generic
        ["Content Moderation"](/api-reference/streaming/ai/create-ai-task) method.

        **What is Soft nudity detection?**

        This method is often used to analyze UGC to determine whether videos can be
        published to all users, or to prohibit publication due to offensive and
        inappropriate content.

        Objects that can be detected:

        - `ANUS_COVERED`
        - `ANUS_EXPOSED`
        - `ARMPITS_COVERED`
        - `ARMPITS_EXPOSED`
        - `BELLY_COVERED`
        - `BELLY_EXPOSED`
        - `BUTTOCKS_COVERED`
        - `BUTTOCKS_EXPOSED`
        - `FACE_FEMALE`
        - `FACE_MALE`
        - `FEET_COVERED`
        - `FEET_EXPOSED`
        - `FEMALE_BREAST_COVERED`
        - `FEMALE_BREAST_EXPOSED`
        - `FEMALE_GENITALIA_COVERED`
        - `FEMALE_GENITALIA_EXPOSED`
        - `MALE_BREAST_EXPOSED`
        - `MALE_GENITALIA_EXPOSED`

        This method allows you to identify faces and other body parts. Used to find
        complex combinations of what is happening in a video. Please note that the
        number of objects is more than in the hard-nudity-detection. The method is
        slower.

        ![AI Content Moderation: hard nudity detection visual example](https://demo-files.gvideo.io/apidocs/soft_nudity_detection.gif)

        **How to use?**

        The information is returned with the video frame number where it was found and
        probability of the detected object. Nudity detection is done using AI, so for
        each object a probability percentage is applied; objects with a probability of
        at least 30% are included in the response.

        Video processing speed is approximately 1:5.

        Example of detected nudity or body parts:

        ```
        {
          "nudity_detected": true,
          "detection_results": [ "FACE_FEMALE", "BELLY_COVERED" ]
          "frames": [
              {
                  "confidence": 0.82,
                  "frame_number": 1,
                  "label": "BELLY_COVERED"
              },...
          ]
        }
        ```

        Example response when nudity or body parts were not found:

        ```
        {
          "nudity_detected": false,
          "detection_results": []
          "frames": []
        }
        ```

        There is no universal recipe under which a video can be considered unacceptable,
        since different services host different types of videos for different audiences:
        adult content, children's content, educational content, etc. You can determine
        the probability threshold at which you consider a video inappropriate. The
        easiest option is to run several of your videos and analyze the resulting
        probability coefficient.

        Sometimes a detected object at the beginning of the video immediately makes it
        clear that there is no need to further analyze the video. For such cases, you
        can use stop tags. Use parameter "stop_objects" to specify comma separated stop
        tags. It is also possible to specify % probability threshold value, above which
        the stop tag will be triggered.

        ```
          {
              "url": "...",
              "stop_objects": "BELLY_COVERED:0.9,FEMALE_GENITALIA_COVERED"
          }
        ```

        Please note that the API only provides a set of data (json) about the objects
        found, so no video is generated. The demo video video (above ^) was specially
        created based on json from the API for visual demonstration and better
        perception of the possibilities.

        Create AI CM:sport task

        This algorithm allows to identify various sporting activities in a video.
        Generic info about all capabilities and limits see in the generic
        ["Content Moderation"](/api-reference/streaming/ai/create-ai-task) method.

        **What is Sports activity detection?**

        Sports activity detection by AI involves using machine learning and computer
        vision technologies to automatically identify, analyze, and interpret various
        activities within sports and generic videos. This can include detecting specific
        types, actions, events, and moments.

        This model operates on a video sequence (and not on images as most of the used
        computer vision models). Make sure your video is at least 10-15 seconds long.

        Sports activities can be detected:

        - archery
        - arm wrestling
        - playing badminton
        - playing baseball
        - basketball dunk
        - bowling
        - boxing punch
        - boxing speed bag
        - catching or throwing baseball
        - catching or throwing softball
        - cricket
        - curling
        - disc golfing
        - dodgeball
        - fencing
        - football
        - golf chipping
        - golf driving
        - golf putting
        - hitting baseball
        - hockey stop
        - ice skating
        - javelin throw
        - juggling soccer ball
        - kayaking
        - kicking field goal
        - kicking soccer ball
        - playing cricket
        - playing field hockey
        - playing ice hockey
        - playing kickball
        - playing lacrosse
        - playing ping pong
        - playing polo
        - playing squash or racquetball
        - playing tennis
        - playing volleyball
        - pole vault
        - riding a bike
        - riding or walking with horse
        - roller skating
        - rowing
        - sailing
        - shooting goal (soccer)
        - skateboarding
        - skiing

        Use cases:

        - Sports leagues and content creators can use AI to monitor UGC for unauthorized
          publications of their content. This can include detecting specific sporting
          events or activities that are part of copyrighted content.
        - Sports fans often miss live games and rely on highlight reels. AI can
          automatically detect key moments like goals, touchdowns, or game-winning shots
          in uploaded UGC videos and compile them into personalized highlight reels.

        ![AI Content Moderation: sports activity detection visual example](https://demo-files.gvideo.io/apidocs/sports_football_detection.gif)

        **How to use?**

        The information is returned with the video frame number where it was found and
        probability of the detected activity. Identification is done using AI, so for
        each activity a probability percentage is applied; activities with a probability
        of at least 30% are included in the response.

        Video processing speed is approximately 1:5.

        Example of detected sports activity:

        ```
        {
          "sport_detected": true,
          "detection_results": [ "shooting goal (soccer)" ],
          "frames": [
              {
                  "label": "shooting goal (soccer)",
                  "frame_number": 98,
                  "confidence": 0.99
              },...
          ]
        }
        ```

        Example response when sports activities were not found:

        ```
        {
          "sport_detected": false,
          "detection_results": []
          "frames": []
        }
        ```

        Please note that the API only provides a set of data (json) about the objects
        found, so no video is generated. The demo video video (above ^) was specially
        created based on json from the API for visual demonstration and better
        perception of the possibilities.

        Args:
          category: AI content moderation with "hard_nudity" algorithm

          task_name: Name of the task to be performed

          url: URL to the MP4 file to analyze. File must be publicly accessible via HTTP/HTTPS.

          client_entity_data: Meta parameter, designed to store your own extra information about a video
              entity: video source, video id, etc. It is not used in any way in video
              processing.

              For example, if an AI-task was created automatically when you uploaded a video
              with the AI auto-processing option (nudity detection, etc), then the ID of the
              associated video for which the task was performed will be explicitly indicated
              here.

          client_user_id: Meta parameter, designed to store your own identifier. Can be used by you to tag
              requests from different end-users. It is not used in any way in video
              processing.

          stop_objects: Comma separated objects, and probabilities, that will cause the processing to
              stop immediately after finding.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        category: Literal["soft_nudity"],
        task_name: Literal["content-moderation"],
        url: str,
        client_entity_data: str | Omit = omit,
        client_user_id: str | Omit = omit,
        stop_objects: Literal[
            "ANUS_COVERED",
            "ANUS_EXPOSED",
            "ARMPITS_COVERED",
            "ARMPITS_EXPOSED",
            "BELLY_COVERED",
            "BELLY_EXPOSED",
            "BUTTOCKS_COVERED",
            "BUTTOCKS_EXPOSED",
            "FACE_FEMALE",
            "FACE_MALE",
            "FEET_COVERED",
            "FEET_EXPOSED",
            "FEMALE_BREAST_COVERED",
            "FEMALE_BREAST_EXPOSED",
            "FEMALE_GENITALIA_COVERED",
            "FEMALE_GENITALIA_EXPOSED",
            "MALE_BREAST_EXPOSED",
            "MALE_GENITALIA_EXPOSED",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AITaskCreateResponse:
        """
        Creating an AI task.

        This method allows you to create an AI task for VOD video processing:

        - ASR: Transcribe video
        - ASR: Translate subtitles
        - CM: Sports detection
        - CM: Not Safe For Work (NSFW) content detection
        - CM: Soft nudity detection
        - CM: Hard nudity detection
        - CM: Objects recognition (soon)

        ![Auto generated subtitles example](https://demo-files.gvideo.io/apidocs/captions.gif)

        How to use:

        - Create an AI task, specify algorithm to use
        - Get `task_id`
        - Check a result using `.../ai/tasks/{task_id}` method

        For more detailed information, see the algorithm-specific sections below.

        **AI Automatic Speech Recognition (ASR)**

        AI is instrumental in automatic video processing for subtitles creation by using
        Automatic Speech Recognition (ASR) technology to transcribe spoken words into
        text, which can then be translated into multiple languages for broader
        accessibility.

        Categories:

        - `transcription` – to create subtitles/captions from audio in the original
          language.
        - `translation` – to translate subtitles/captions from the original language to
          99+ other languages.

        AI subtitle transcription and translation tools are highly efficient, processing
        large volumes of audio-visual content quickly and providing accurate
        transcriptions and translations with minimal human intervention. Additionally,
        AI-driven solutions can significantly reduce costs and turnaround times compared
        to traditional methods, making them an invaluable resource for content creators
        and broadcasters aiming to reach global audiences.

        Example response with positive result:

        ```
        {
          "status": "SUCCESS",
          "result": {
            "subtitles": [
              {
                  "start_time": "00:00:00.031",
                  "end_time": "00:00:03.831",
                  "text": "Come on team, ..."
              }, ...
            ]
            "vttContent": "WEBVTT\n\n1\n00:00:00.031 --> 00:00:03.831\nCome on team, ...",
            "concatenated_text": "Come on team, ...",
            "languages": [ "eng" ],
            "speech_detected": true
            }
          }, ...
        }
        ```

        **AI Content Moderation (CM)**

        The AI Content Moderation API offers a powerful solution for analyzing video
        content to detect various categories of inappropriate material. Leveraging
        state-of-the-art AI models, this API ensures real-time analysis and flagging of
        sensitive or restricted content types, making it an essential tool for platforms
        requiring stringent content moderation.

        Categories:

        - `nsfw`: Quick algorithm to detect pornographic material, ensuring content is
          "not-safe-for-work" or normal.
        - `hard_nudity`: Detailed analysis of video which detects explicit nudity
          involving genitalia.
        - `soft_nudity`: Detailed video analysis that reveals both explicit and partial
          nudity, including the presence of male and female faces and other uncovered
          body parts.
        - `sport`: Recognizes various sporting activities.

        The AI Content Moderation API is an invaluable tool for managing and controlling
        the type of content being shared or streamed on your platform. By implementing
        this API, you can ensure compliance with community guidelines and legal
        requirements, as well as provide a safer environment for your users.

        Important notes:

        - It's allowed to analyze still images too (where applicable). Format of image:
          JPEG, PNG. In that case one image is the same as video of 1 second duration.
        - Not all frames in the video are used for analysis, but only key frames
          (Iframe). For example, if a key frame in a video is set every ±2 seconds, then
          detection will only occur at these timestamps. If an object appears and
          disappears between these time stamps, it will not be detected. We are working
          on a version to analyze more frames, please contact your manager or our
          support team to enable this method.

        Example response with positive result:

        ```
        {
          "status": "SUCCESS",
          "result": {
              "nsfw_detected": true,
              "detection_results": [ "nsfw" ],
              "frames": [
                  {
                      "label": "nsfw",
                      "confidence": 1.0,
                      "frame_number": 24
                  },...
              ]
          }
        }
        ```

        **Additional information**

        Billing takes into account the duration of the analyzed video. Or the duration
        until the stop tag(where applicable), if the condition was triggered during the
        analysis.

        The heart of content moderation is AI, with additional services. They run on our
        own infrastructure, so the files/data are not transferred anywhere to external
        services. After processing, original files are also deleted from local storage
        of AI.

        Read more detailed information about our solution, and architecture, and
        benefits in the knowledge base and blog.

        **Algorithm-specific details**

        Create AI ASR task

        Transcribing is the process of writing down the words you hear in an audio. Our
        solution allows you to transcribe audio from your video and get subtitles
        automatically. To do this, we use modern AI models.

        The result:

        - Transcription – subtitles in the original language. I.e. audio is in English –
          subtitles are in English too, audio is in German – subtitles are in German
          too.
        - Translation – subtitles is translated from the original language to any other
          language.

        **How to use?**

        - Explicit call to this AI method. Applicable for any file stored with us or
          located on the Internet.
        - Standard video upload but with automatic subtitle generation. Look at
          ["VOD uploading"](/api-reference/streaming/videos/create-video).

        **What language will the subtitles be in?**

        You can specify the language explicitly, then it will be used to create
        subtitles: the source language in the audio, the resulting subtitle language. If
        this is not set, the system will run auto language identification and the
        subtitles will be in the detected language. The method also works based on AI
        analysis.

        Additionally, when this is not set, we also support recognition of alternate
        languages in the video (code-switching). For example, when in a video different
        speakers speak several languages, or when they switch from their native language
        to English and back. Thus when you have multiple languages in the video it is
        better to not specify an "audio_language" otherwise AI may force the system to
        recognize gibberish.

        **What can be transcribed?**

        Service uses additional methods to detect presence of speech in audio track,
        thus improving the detection of any human conversations:

        - Speech of one speaker,
        - Speech of several speakers,
        - Speech in different languages,
        - etc

        Restriction on music, lyrics most likely will not be created.

        **What about translation?**

        It is also possible to automatically translate from the original language to
        another you need.

        To create a translation, specify the desired language explicitly in
        "subtitles_language" parameter. Otherwise, the subtitles will be in the original
        language. Translation into different languages should be done by creating
        separate tasks.

        ![Auto generated subtitles example](https://demo-files.gvideo.io/apidocs/captions.gif)

        Use MP4 videos to process. This method is not tied to videos that are stored
        only in our video hosting (look at how get a link to MP4 rendition), so you can
        use links to any other external file with HTTP/HTTPS access.

        For now, only the first audio track can be processed; later this functionality
        will be improved to allow to use any. Also, not all language pairs are currently
        supported. If a language pair is not supported for automatic translation, the
        task status will be FAILURE with description of the reason. Example:
        `eng => uzb`. You can request to add the language pair you need for automatic
        translation. Contact our support.

        Example of modes to transcribe and/or translate:

        - Auto language detection: `{ "url":"..." }`
        - From German language explicitly : `{ "url":"...", "audio_language":"ger" }`
        - From any auto-detected to English language explicitly:
          `{ "url":"...", "subtitles_language":"eng" }`
        - From German language to English language explicitly:
          `{ "url":"...", "audio_language":"ger", "subtitles_language":"eng" }`

        Example of setting a task to process MP4 file (animated gif from above):

        ```
        curl -L 'https://api.gcore.com/streaming/ai/tasks' \\
        -H 'Content-Type: application/json' \\
        -H 'Authorization: APIKey 1234$abcd...' \\
        -d '{
            "url": "https://demo-files.gvideo.io/apidocs/spritefright-blender-cut30sec.mp4"
        }'
        ```

        As described above, transcription is done automatically using AI. Therefore, the
        quality may differ from a manual transcription by a professional person. If this
        happens to you, then you can download subtitles and change them in an external
        editor.

        Transcription and translation are 2 different AI tasks:

        - Transcription is set only for transcription.
        - Translation, if non-original languages are set for translation.

        Billing takes into account the duration of the analyzed original video.

        The heart for transcribing is the AI model Whisper from OpenAI, with additional
        optimizations and services. The AI models run on our own infrastructure, so the
        files/data are not transferred anywhere to external services. After processing,
        original files are also deleted from local storage of AI.

        Read more detailed information about our solution, and architecture, and
        benefits in the knowledge base and blog.

        Create AI CM:nsfw task

        This algorithm allows to quickly detect inappropriate content, determining that
        the content is NSFW ("Not Safe For Work") or normal. Generic info about all
        capabilities and limits see in the generic
        ["Content Moderation"](/api-reference/streaming/ai/create-ai-task) method.

        **What is "Not Safe For Work"?**

        The algorithm has recognized inappropriate content in a video and it might not
        be suitable to view in public places. The solution provides its confidence level
        (in percentage) of how sure it is that the content is NSFW, or it most likely
        does not contain any sexual or similar content.

        Different to soft-nudity-detection and hard-nudity-detection, this model will
        only check for sensitive material that can be considered not-safe-for-work.

        ![AI Content Moderation: NSFW detection visual example](https://demo-files.gvideo.io/apidocs/nsfw-detection.gif)

        **How to use?**

        Frames within the specified video are analyzed.

        Response will contain only frames for which the class nsfw is detected with a
        confidence of more than 50%.

        Example of detected NSFW:

        ```
        {
          "nsfw_detected": true,
          "detection_results": [ "nsfw" ],
          "frames": [
              {
                  "label": "nsfw",
                  "confidence": 0.93,
                  "frame_number": 1
              },..
          ]
        }
        ```

        Example of a response without detecting inappropriate content:

        ```
        {
          "nsfw_detected": false,
          "detection_results": [],
          "frames": []
        }
        ```

        Please note that the API only provides a set of data (json) about the objects
        found, so no video is generated. The demo video video (above ^) was specially
        created based on json from the API for visual demonstration and better
        perception of the possibilities.

        Create AI CM:`hard_nudity` task

        This algorithm allows to detect explicit nudity of the human body (involving
        genitals) in a video. Generic info about all capabilities and limits see in the
        generic ["Content Moderation"](/api-reference/streaming/ai/create-ai-task)
        method.

        **What is Hard nudity detection?**

        This method is often used to analyze UGC to determine whether videos can be
        published to all users, or to prohibit publication due to offensive and
        inappropriate content.

        Objects that can be detected:

        - `ANUS_EXPOSED`
        - `BUTTOCKS_EXPOSED`
        - `FEMALE_BREAST_EXPOSED`
        - `FEMALE_GENITALIA_EXPOSED`
        - `MALE_BREAST_EXPOSED`
        - `MALE_GENITALIA_EXPOSED`

        Please note that the number of objects is less than in the
        soft-nudity-detection. This method works faster and better if only exposed body
        parts detection is required.

        ![AI Content Moderation: hard nudity detection visual example](https://demo-files.gvideo.io/apidocs/nudity_detection.gif)

        **How to use?**

        The information is returned with the video frame number where it was found and
        probability of the detected object. Nudity detection is done using AI, so for
        each object a probability percentage is applied; objects with a probability of
        at least 30% are included in the response.

        Video processing speed is approximately 1:5.

        Example of detected nudity or body parts:

        ```
        {
          "nudity_detected": true,
          "detection_results": [ "MALE_GENITALIA_EXPOSED" ]
          "frames": [
              {
                  "confidence": 0.75,
                  "frame_number": 35,
                  "label": "MALE_GENITALIA_EXPOSED"
              },...
          ]
        }
        ```

        Example response when nudity or body parts were not found:

        ```
        {
          "nudity_detected": false,
          "detection_results": []
          "frames": []
        }
        ```

        There is no universal recipe under which a video can be considered unacceptable,
        since different services host different types of videos for different audiences:
        adult content, children's content, educational content, etc. You can determine
        the probability threshold at which you consider a video inappropriate. The
        easiest option is to run several of your videos and analyze the resulting
        probability coefficient.

        Sometimes a detected object at the beginning of the video immediately makes it
        clear that there is no need to further analyze the video. For such cases, you
        can use stop tags. Use parameter "stop_objects" to specify comma separated stop
        tags. It is also possible to specify % probability threshold value, above which
        the stop tag will be triggered.

        ```
          {
              "url": "...",
              "stop_objects": "MALE_GENITALIA_EXPOSED:0.8,FEMALE_GENITALIA_EXPOSED"
          }
        ```

        Please note that the API only provides a set of data (json) about the objects
        found, so no video is generated. The demo video video (above ^) was specially
        created based on json from the API for visual demonstration and better
        perception of the possibilities.

        Create AI CM:`soft_nudity` task

        This algorithm allows to identify explicit nudity and partial nudity too
        (including the presence of male and female faces and other uncovered body parts)
        in a video. Generic info about all capabilities and limits see in the generic
        ["Content Moderation"](/api-reference/streaming/ai/create-ai-task) method.

        **What is Soft nudity detection?**

        This method is often used to analyze UGC to determine whether videos can be
        published to all users, or to prohibit publication due to offensive and
        inappropriate content.

        Objects that can be detected:

        - `ANUS_COVERED`
        - `ANUS_EXPOSED`
        - `ARMPITS_COVERED`
        - `ARMPITS_EXPOSED`
        - `BELLY_COVERED`
        - `BELLY_EXPOSED`
        - `BUTTOCKS_COVERED`
        - `BUTTOCKS_EXPOSED`
        - `FACE_FEMALE`
        - `FACE_MALE`
        - `FEET_COVERED`
        - `FEET_EXPOSED`
        - `FEMALE_BREAST_COVERED`
        - `FEMALE_BREAST_EXPOSED`
        - `FEMALE_GENITALIA_COVERED`
        - `FEMALE_GENITALIA_EXPOSED`
        - `MALE_BREAST_EXPOSED`
        - `MALE_GENITALIA_EXPOSED`

        This method allows you to identify faces and other body parts. Used to find
        complex combinations of what is happening in a video. Please note that the
        number of objects is more than in the hard-nudity-detection. The method is
        slower.

        ![AI Content Moderation: hard nudity detection visual example](https://demo-files.gvideo.io/apidocs/soft_nudity_detection.gif)

        **How to use?**

        The information is returned with the video frame number where it was found and
        probability of the detected object. Nudity detection is done using AI, so for
        each object a probability percentage is applied; objects with a probability of
        at least 30% are included in the response.

        Video processing speed is approximately 1:5.

        Example of detected nudity or body parts:

        ```
        {
          "nudity_detected": true,
          "detection_results": [ "FACE_FEMALE", "BELLY_COVERED" ]
          "frames": [
              {
                  "confidence": 0.82,
                  "frame_number": 1,
                  "label": "BELLY_COVERED"
              },...
          ]
        }
        ```

        Example response when nudity or body parts were not found:

        ```
        {
          "nudity_detected": false,
          "detection_results": []
          "frames": []
        }
        ```

        There is no universal recipe under which a video can be considered unacceptable,
        since different services host different types of videos for different audiences:
        adult content, children's content, educational content, etc. You can determine
        the probability threshold at which you consider a video inappropriate. The
        easiest option is to run several of your videos and analyze the resulting
        probability coefficient.

        Sometimes a detected object at the beginning of the video immediately makes it
        clear that there is no need to further analyze the video. For such cases, you
        can use stop tags. Use parameter "stop_objects" to specify comma separated stop
        tags. It is also possible to specify % probability threshold value, above which
        the stop tag will be triggered.

        ```
          {
              "url": "...",
              "stop_objects": "BELLY_COVERED:0.9,FEMALE_GENITALIA_COVERED"
          }
        ```

        Please note that the API only provides a set of data (json) about the objects
        found, so no video is generated. The demo video video (above ^) was specially
        created based on json from the API for visual demonstration and better
        perception of the possibilities.

        Create AI CM:sport task

        This algorithm allows to identify various sporting activities in a video.
        Generic info about all capabilities and limits see in the generic
        ["Content Moderation"](/api-reference/streaming/ai/create-ai-task) method.

        **What is Sports activity detection?**

        Sports activity detection by AI involves using machine learning and computer
        vision technologies to automatically identify, analyze, and interpret various
        activities within sports and generic videos. This can include detecting specific
        types, actions, events, and moments.

        This model operates on a video sequence (and not on images as most of the used
        computer vision models). Make sure your video is at least 10-15 seconds long.

        Sports activities can be detected:

        - archery
        - arm wrestling
        - playing badminton
        - playing baseball
        - basketball dunk
        - bowling
        - boxing punch
        - boxing speed bag
        - catching or throwing baseball
        - catching or throwing softball
        - cricket
        - curling
        - disc golfing
        - dodgeball
        - fencing
        - football
        - golf chipping
        - golf driving
        - golf putting
        - hitting baseball
        - hockey stop
        - ice skating
        - javelin throw
        - juggling soccer ball
        - kayaking
        - kicking field goal
        - kicking soccer ball
        - playing cricket
        - playing field hockey
        - playing ice hockey
        - playing kickball
        - playing lacrosse
        - playing ping pong
        - playing polo
        - playing squash or racquetball
        - playing tennis
        - playing volleyball
        - pole vault
        - riding a bike
        - riding or walking with horse
        - roller skating
        - rowing
        - sailing
        - shooting goal (soccer)
        - skateboarding
        - skiing

        Use cases:

        - Sports leagues and content creators can use AI to monitor UGC for unauthorized
          publications of their content. This can include detecting specific sporting
          events or activities that are part of copyrighted content.
        - Sports fans often miss live games and rely on highlight reels. AI can
          automatically detect key moments like goals, touchdowns, or game-winning shots
          in uploaded UGC videos and compile them into personalized highlight reels.

        ![AI Content Moderation: sports activity detection visual example](https://demo-files.gvideo.io/apidocs/sports_football_detection.gif)

        **How to use?**

        The information is returned with the video frame number where it was found and
        probability of the detected activity. Identification is done using AI, so for
        each activity a probability percentage is applied; activities with a probability
        of at least 30% are included in the response.

        Video processing speed is approximately 1:5.

        Example of detected sports activity:

        ```
        {
          "sport_detected": true,
          "detection_results": [ "shooting goal (soccer)" ],
          "frames": [
              {
                  "label": "shooting goal (soccer)",
                  "frame_number": 98,
                  "confidence": 0.99
              },...
          ]
        }
        ```

        Example response when sports activities were not found:

        ```
        {
          "sport_detected": false,
          "detection_results": []
          "frames": []
        }
        ```

        Please note that the API only provides a set of data (json) about the objects
        found, so no video is generated. The demo video video (above ^) was specially
        created based on json from the API for visual demonstration and better
        perception of the possibilities.

        Args:
          category: AI content moderation with "soft_nudity" algorithm

          task_name: Name of the task to be performed

          url: URL to the MP4 file to analyze. File must be publicly accessible via HTTP/HTTPS.

          client_entity_data: Meta parameter, designed to store your own extra information about a video
              entity: video source, video id, etc. It is not used in any way in video
              processing.

              For example, if an AI-task was created automatically when you uploaded a video
              with the AI auto-processing option (nudity detection, etc), then the ID of the
              associated video for which the task was performed will be explicitly indicated
              here.

          client_user_id: Meta parameter, designed to store your own identifier. Can be used by you to tag
              requests from different end-users. It is not used in any way in video
              processing.

          stop_objects: Comma separated objects, and probabilities, that will cause the processing to
              stop immediately after finding.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        category: Literal["sport"],
        task_name: Literal["content-moderation"],
        url: str,
        client_entity_data: str | Omit = omit,
        client_user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AITaskCreateResponse:
        """
        Creating an AI task.

        This method allows you to create an AI task for VOD video processing:

        - ASR: Transcribe video
        - ASR: Translate subtitles
        - CM: Sports detection
        - CM: Not Safe For Work (NSFW) content detection
        - CM: Soft nudity detection
        - CM: Hard nudity detection
        - CM: Objects recognition (soon)

        ![Auto generated subtitles example](https://demo-files.gvideo.io/apidocs/captions.gif)

        How to use:

        - Create an AI task, specify algorithm to use
        - Get `task_id`
        - Check a result using `.../ai/tasks/{task_id}` method

        For more detailed information, see the algorithm-specific sections below.

        **AI Automatic Speech Recognition (ASR)**

        AI is instrumental in automatic video processing for subtitles creation by using
        Automatic Speech Recognition (ASR) technology to transcribe spoken words into
        text, which can then be translated into multiple languages for broader
        accessibility.

        Categories:

        - `transcription` – to create subtitles/captions from audio in the original
          language.
        - `translation` – to translate subtitles/captions from the original language to
          99+ other languages.

        AI subtitle transcription and translation tools are highly efficient, processing
        large volumes of audio-visual content quickly and providing accurate
        transcriptions and translations with minimal human intervention. Additionally,
        AI-driven solutions can significantly reduce costs and turnaround times compared
        to traditional methods, making them an invaluable resource for content creators
        and broadcasters aiming to reach global audiences.

        Example response with positive result:

        ```
        {
          "status": "SUCCESS",
          "result": {
            "subtitles": [
              {
                  "start_time": "00:00:00.031",
                  "end_time": "00:00:03.831",
                  "text": "Come on team, ..."
              }, ...
            ]
            "vttContent": "WEBVTT\n\n1\n00:00:00.031 --> 00:00:03.831\nCome on team, ...",
            "concatenated_text": "Come on team, ...",
            "languages": [ "eng" ],
            "speech_detected": true
            }
          }, ...
        }
        ```

        **AI Content Moderation (CM)**

        The AI Content Moderation API offers a powerful solution for analyzing video
        content to detect various categories of inappropriate material. Leveraging
        state-of-the-art AI models, this API ensures real-time analysis and flagging of
        sensitive or restricted content types, making it an essential tool for platforms
        requiring stringent content moderation.

        Categories:

        - `nsfw`: Quick algorithm to detect pornographic material, ensuring content is
          "not-safe-for-work" or normal.
        - `hard_nudity`: Detailed analysis of video which detects explicit nudity
          involving genitalia.
        - `soft_nudity`: Detailed video analysis that reveals both explicit and partial
          nudity, including the presence of male and female faces and other uncovered
          body parts.
        - `sport`: Recognizes various sporting activities.

        The AI Content Moderation API is an invaluable tool for managing and controlling
        the type of content being shared or streamed on your platform. By implementing
        this API, you can ensure compliance with community guidelines and legal
        requirements, as well as provide a safer environment for your users.

        Important notes:

        - It's allowed to analyze still images too (where applicable). Format of image:
          JPEG, PNG. In that case one image is the same as video of 1 second duration.
        - Not all frames in the video are used for analysis, but only key frames
          (Iframe). For example, if a key frame in a video is set every ±2 seconds, then
          detection will only occur at these timestamps. If an object appears and
          disappears between these time stamps, it will not be detected. We are working
          on a version to analyze more frames, please contact your manager or our
          support team to enable this method.

        Example response with positive result:

        ```
        {
          "status": "SUCCESS",
          "result": {
              "nsfw_detected": true,
              "detection_results": [ "nsfw" ],
              "frames": [
                  {
                      "label": "nsfw",
                      "confidence": 1.0,
                      "frame_number": 24
                  },...
              ]
          }
        }
        ```

        **Additional information**

        Billing takes into account the duration of the analyzed video. Or the duration
        until the stop tag(where applicable), if the condition was triggered during the
        analysis.

        The heart of content moderation is AI, with additional services. They run on our
        own infrastructure, so the files/data are not transferred anywhere to external
        services. After processing, original files are also deleted from local storage
        of AI.

        Read more detailed information about our solution, and architecture, and
        benefits in the knowledge base and blog.

        **Algorithm-specific details**

        Create AI ASR task

        Transcribing is the process of writing down the words you hear in an audio. Our
        solution allows you to transcribe audio from your video and get subtitles
        automatically. To do this, we use modern AI models.

        The result:

        - Transcription – subtitles in the original language. I.e. audio is in English –
          subtitles are in English too, audio is in German – subtitles are in German
          too.
        - Translation – subtitles is translated from the original language to any other
          language.

        **How to use?**

        - Explicit call to this AI method. Applicable for any file stored with us or
          located on the Internet.
        - Standard video upload but with automatic subtitle generation. Look at
          ["VOD uploading"](/api-reference/streaming/videos/create-video).

        **What language will the subtitles be in?**

        You can specify the language explicitly, then it will be used to create
        subtitles: the source language in the audio, the resulting subtitle language. If
        this is not set, the system will run auto language identification and the
        subtitles will be in the detected language. The method also works based on AI
        analysis.

        Additionally, when this is not set, we also support recognition of alternate
        languages in the video (code-switching). For example, when in a video different
        speakers speak several languages, or when they switch from their native language
        to English and back. Thus when you have multiple languages in the video it is
        better to not specify an "audio_language" otherwise AI may force the system to
        recognize gibberish.

        **What can be transcribed?**

        Service uses additional methods to detect presence of speech in audio track,
        thus improving the detection of any human conversations:

        - Speech of one speaker,
        - Speech of several speakers,
        - Speech in different languages,
        - etc

        Restriction on music, lyrics most likely will not be created.

        **What about translation?**

        It is also possible to automatically translate from the original language to
        another you need.

        To create a translation, specify the desired language explicitly in
        "subtitles_language" parameter. Otherwise, the subtitles will be in the original
        language. Translation into different languages should be done by creating
        separate tasks.

        ![Auto generated subtitles example](https://demo-files.gvideo.io/apidocs/captions.gif)

        Use MP4 videos to process. This method is not tied to videos that are stored
        only in our video hosting (look at how get a link to MP4 rendition), so you can
        use links to any other external file with HTTP/HTTPS access.

        For now, only the first audio track can be processed; later this functionality
        will be improved to allow to use any. Also, not all language pairs are currently
        supported. If a language pair is not supported for automatic translation, the
        task status will be FAILURE with description of the reason. Example:
        `eng => uzb`. You can request to add the language pair you need for automatic
        translation. Contact our support.

        Example of modes to transcribe and/or translate:

        - Auto language detection: `{ "url":"..." }`
        - From German language explicitly : `{ "url":"...", "audio_language":"ger" }`
        - From any auto-detected to English language explicitly:
          `{ "url":"...", "subtitles_language":"eng" }`
        - From German language to English language explicitly:
          `{ "url":"...", "audio_language":"ger", "subtitles_language":"eng" }`

        Example of setting a task to process MP4 file (animated gif from above):

        ```
        curl -L 'https://api.gcore.com/streaming/ai/tasks' \\
        -H 'Content-Type: application/json' \\
        -H 'Authorization: APIKey 1234$abcd...' \\
        -d '{
            "url": "https://demo-files.gvideo.io/apidocs/spritefright-blender-cut30sec.mp4"
        }'
        ```

        As described above, transcription is done automatically using AI. Therefore, the
        quality may differ from a manual transcription by a professional person. If this
        happens to you, then you can download subtitles and change them in an external
        editor.

        Transcription and translation are 2 different AI tasks:

        - Transcription is set only for transcription.
        - Translation, if non-original languages are set for translation.

        Billing takes into account the duration of the analyzed original video.

        The heart for transcribing is the AI model Whisper from OpenAI, with additional
        optimizations and services. The AI models run on our own infrastructure, so the
        files/data are not transferred anywhere to external services. After processing,
        original files are also deleted from local storage of AI.

        Read more detailed information about our solution, and architecture, and
        benefits in the knowledge base and blog.

        Create AI CM:nsfw task

        This algorithm allows to quickly detect inappropriate content, determining that
        the content is NSFW ("Not Safe For Work") or normal. Generic info about all
        capabilities and limits see in the generic
        ["Content Moderation"](/api-reference/streaming/ai/create-ai-task) method.

        **What is "Not Safe For Work"?**

        The algorithm has recognized inappropriate content in a video and it might not
        be suitable to view in public places. The solution provides its confidence level
        (in percentage) of how sure it is that the content is NSFW, or it most likely
        does not contain any sexual or similar content.

        Different to soft-nudity-detection and hard-nudity-detection, this model will
        only check for sensitive material that can be considered not-safe-for-work.

        ![AI Content Moderation: NSFW detection visual example](https://demo-files.gvideo.io/apidocs/nsfw-detection.gif)

        **How to use?**

        Frames within the specified video are analyzed.

        Response will contain only frames for which the class nsfw is detected with a
        confidence of more than 50%.

        Example of detected NSFW:

        ```
        {
          "nsfw_detected": true,
          "detection_results": [ "nsfw" ],
          "frames": [
              {
                  "label": "nsfw",
                  "confidence": 0.93,
                  "frame_number": 1
              },..
          ]
        }
        ```

        Example of a response without detecting inappropriate content:

        ```
        {
          "nsfw_detected": false,
          "detection_results": [],
          "frames": []
        }
        ```

        Please note that the API only provides a set of data (json) about the objects
        found, so no video is generated. The demo video video (above ^) was specially
        created based on json from the API for visual demonstration and better
        perception of the possibilities.

        Create AI CM:`hard_nudity` task

        This algorithm allows to detect explicit nudity of the human body (involving
        genitals) in a video. Generic info about all capabilities and limits see in the
        generic ["Content Moderation"](/api-reference/streaming/ai/create-ai-task)
        method.

        **What is Hard nudity detection?**

        This method is often used to analyze UGC to determine whether videos can be
        published to all users, or to prohibit publication due to offensive and
        inappropriate content.

        Objects that can be detected:

        - `ANUS_EXPOSED`
        - `BUTTOCKS_EXPOSED`
        - `FEMALE_BREAST_EXPOSED`
        - `FEMALE_GENITALIA_EXPOSED`
        - `MALE_BREAST_EXPOSED`
        - `MALE_GENITALIA_EXPOSED`

        Please note that the number of objects is less than in the
        soft-nudity-detection. This method works faster and better if only exposed body
        parts detection is required.

        ![AI Content Moderation: hard nudity detection visual example](https://demo-files.gvideo.io/apidocs/nudity_detection.gif)

        **How to use?**

        The information is returned with the video frame number where it was found and
        probability of the detected object. Nudity detection is done using AI, so for
        each object a probability percentage is applied; objects with a probability of
        at least 30% are included in the response.

        Video processing speed is approximately 1:5.

        Example of detected nudity or body parts:

        ```
        {
          "nudity_detected": true,
          "detection_results": [ "MALE_GENITALIA_EXPOSED" ]
          "frames": [
              {
                  "confidence": 0.75,
                  "frame_number": 35,
                  "label": "MALE_GENITALIA_EXPOSED"
              },...
          ]
        }
        ```

        Example response when nudity or body parts were not found:

        ```
        {
          "nudity_detected": false,
          "detection_results": []
          "frames": []
        }
        ```

        There is no universal recipe under which a video can be considered unacceptable,
        since different services host different types of videos for different audiences:
        adult content, children's content, educational content, etc. You can determine
        the probability threshold at which you consider a video inappropriate. The
        easiest option is to run several of your videos and analyze the resulting
        probability coefficient.

        Sometimes a detected object at the beginning of the video immediately makes it
        clear that there is no need to further analyze the video. For such cases, you
        can use stop tags. Use parameter "stop_objects" to specify comma separated stop
        tags. It is also possible to specify % probability threshold value, above which
        the stop tag will be triggered.

        ```
          {
              "url": "...",
              "stop_objects": "MALE_GENITALIA_EXPOSED:0.8,FEMALE_GENITALIA_EXPOSED"
          }
        ```

        Please note that the API only provides a set of data (json) about the objects
        found, so no video is generated. The demo video video (above ^) was specially
        created based on json from the API for visual demonstration and better
        perception of the possibilities.

        Create AI CM:`soft_nudity` task

        This algorithm allows to identify explicit nudity and partial nudity too
        (including the presence of male and female faces and other uncovered body parts)
        in a video. Generic info about all capabilities and limits see in the generic
        ["Content Moderation"](/api-reference/streaming/ai/create-ai-task) method.

        **What is Soft nudity detection?**

        This method is often used to analyze UGC to determine whether videos can be
        published to all users, or to prohibit publication due to offensive and
        inappropriate content.

        Objects that can be detected:

        - `ANUS_COVERED`
        - `ANUS_EXPOSED`
        - `ARMPITS_COVERED`
        - `ARMPITS_EXPOSED`
        - `BELLY_COVERED`
        - `BELLY_EXPOSED`
        - `BUTTOCKS_COVERED`
        - `BUTTOCKS_EXPOSED`
        - `FACE_FEMALE`
        - `FACE_MALE`
        - `FEET_COVERED`
        - `FEET_EXPOSED`
        - `FEMALE_BREAST_COVERED`
        - `FEMALE_BREAST_EXPOSED`
        - `FEMALE_GENITALIA_COVERED`
        - `FEMALE_GENITALIA_EXPOSED`
        - `MALE_BREAST_EXPOSED`
        - `MALE_GENITALIA_EXPOSED`

        This method allows you to identify faces and other body parts. Used to find
        complex combinations of what is happening in a video. Please note that the
        number of objects is more than in the hard-nudity-detection. The method is
        slower.

        ![AI Content Moderation: hard nudity detection visual example](https://demo-files.gvideo.io/apidocs/soft_nudity_detection.gif)

        **How to use?**

        The information is returned with the video frame number where it was found and
        probability of the detected object. Nudity detection is done using AI, so for
        each object a probability percentage is applied; objects with a probability of
        at least 30% are included in the response.

        Video processing speed is approximately 1:5.

        Example of detected nudity or body parts:

        ```
        {
          "nudity_detected": true,
          "detection_results": [ "FACE_FEMALE", "BELLY_COVERED" ]
          "frames": [
              {
                  "confidence": 0.82,
                  "frame_number": 1,
                  "label": "BELLY_COVERED"
              },...
          ]
        }
        ```

        Example response when nudity or body parts were not found:

        ```
        {
          "nudity_detected": false,
          "detection_results": []
          "frames": []
        }
        ```

        There is no universal recipe under which a video can be considered unacceptable,
        since different services host different types of videos for different audiences:
        adult content, children's content, educational content, etc. You can determine
        the probability threshold at which you consider a video inappropriate. The
        easiest option is to run several of your videos and analyze the resulting
        probability coefficient.

        Sometimes a detected object at the beginning of the video immediately makes it
        clear that there is no need to further analyze the video. For such cases, you
        can use stop tags. Use parameter "stop_objects" to specify comma separated stop
        tags. It is also possible to specify % probability threshold value, above which
        the stop tag will be triggered.

        ```
          {
              "url": "...",
              "stop_objects": "BELLY_COVERED:0.9,FEMALE_GENITALIA_COVERED"
          }
        ```

        Please note that the API only provides a set of data (json) about the objects
        found, so no video is generated. The demo video video (above ^) was specially
        created based on json from the API for visual demonstration and better
        perception of the possibilities.

        Create AI CM:sport task

        This algorithm allows to identify various sporting activities in a video.
        Generic info about all capabilities and limits see in the generic
        ["Content Moderation"](/api-reference/streaming/ai/create-ai-task) method.

        **What is Sports activity detection?**

        Sports activity detection by AI involves using machine learning and computer
        vision technologies to automatically identify, analyze, and interpret various
        activities within sports and generic videos. This can include detecting specific
        types, actions, events, and moments.

        This model operates on a video sequence (and not on images as most of the used
        computer vision models). Make sure your video is at least 10-15 seconds long.

        Sports activities can be detected:

        - archery
        - arm wrestling
        - playing badminton
        - playing baseball
        - basketball dunk
        - bowling
        - boxing punch
        - boxing speed bag
        - catching or throwing baseball
        - catching or throwing softball
        - cricket
        - curling
        - disc golfing
        - dodgeball
        - fencing
        - football
        - golf chipping
        - golf driving
        - golf putting
        - hitting baseball
        - hockey stop
        - ice skating
        - javelin throw
        - juggling soccer ball
        - kayaking
        - kicking field goal
        - kicking soccer ball
        - playing cricket
        - playing field hockey
        - playing ice hockey
        - playing kickball
        - playing lacrosse
        - playing ping pong
        - playing polo
        - playing squash or racquetball
        - playing tennis
        - playing volleyball
        - pole vault
        - riding a bike
        - riding or walking with horse
        - roller skating
        - rowing
        - sailing
        - shooting goal (soccer)
        - skateboarding
        - skiing

        Use cases:

        - Sports leagues and content creators can use AI to monitor UGC for unauthorized
          publications of their content. This can include detecting specific sporting
          events or activities that are part of copyrighted content.
        - Sports fans often miss live games and rely on highlight reels. AI can
          automatically detect key moments like goals, touchdowns, or game-winning shots
          in uploaded UGC videos and compile them into personalized highlight reels.

        ![AI Content Moderation: sports activity detection visual example](https://demo-files.gvideo.io/apidocs/sports_football_detection.gif)

        **How to use?**

        The information is returned with the video frame number where it was found and
        probability of the detected activity. Identification is done using AI, so for
        each activity a probability percentage is applied; activities with a probability
        of at least 30% are included in the response.

        Video processing speed is approximately 1:5.

        Example of detected sports activity:

        ```
        {
          "sport_detected": true,
          "detection_results": [ "shooting goal (soccer)" ],
          "frames": [
              {
                  "label": "shooting goal (soccer)",
                  "frame_number": 98,
                  "confidence": 0.99
              },...
          ]
        }
        ```

        Example response when sports activities were not found:

        ```
        {
          "sport_detected": false,
          "detection_results": []
          "frames": []
        }
        ```

        Please note that the API only provides a set of data (json) about the objects
        found, so no video is generated. The demo video video (above ^) was specially
        created based on json from the API for visual demonstration and better
        perception of the possibilities.

        Args:
          category: AI content moderation with types of sports activity detection

          task_name: Name of the task to be performed

          url: URL to the MP4 file to analyze. File must be publicly accessible via HTTP/HTTPS.

          client_entity_data: Meta parameter, designed to store your own extra information about a video
              entity: video source, video id, etc. It is not used in any way in video
              processing.

              For example, if an AI-task was created automatically when you uploaded a video
              with the AI auto-processing option (nudity detection, etc), then the ID of the
              associated video for which the task was performed will be explicitly indicated
              here.

          client_user_id: Meta parameter, designed to store your own identifier. Can be used by you to tag
              requests from different end-users. It is not used in any way in video
              processing.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["task_name", "url"], ["category", "task_name", "url"])
    def create(
        self,
        *,
        task_name: Literal["transcription"] | Literal["content-moderation"],
        url: str,
        audio_language: str | Omit = omit,
        client_entity_data: str | Omit = omit,
        client_user_id: str | Omit = omit,
        subtitles_language: str | Omit = omit,
        category: Literal["nsfw"] | Literal["hard_nudity"] | Literal["soft_nudity"] | Literal["sport"] | Omit = omit,
        stop_objects: Literal[
            "ANUS_EXPOSED",
            "BUTTOCKS_EXPOSED",
            "FEMALE_BREAST_EXPOSED",
            "FEMALE_GENITALIA_EXPOSED",
            "MALE_BREAST_EXPOSED",
            "MALE_GENITALIA_EXPOSED",
        ]
        | Literal[
            "ANUS_COVERED",
            "ANUS_EXPOSED",
            "ARMPITS_COVERED",
            "ARMPITS_EXPOSED",
            "BELLY_COVERED",
            "BELLY_EXPOSED",
            "BUTTOCKS_COVERED",
            "BUTTOCKS_EXPOSED",
            "FACE_FEMALE",
            "FACE_MALE",
            "FEET_COVERED",
            "FEET_EXPOSED",
            "FEMALE_BREAST_COVERED",
            "FEMALE_BREAST_EXPOSED",
            "FEMALE_GENITALIA_COVERED",
            "FEMALE_GENITALIA_EXPOSED",
            "MALE_BREAST_EXPOSED",
            "MALE_GENITALIA_EXPOSED",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AITaskCreateResponse:
        return self._post(
            "/streaming/ai/tasks",
            body=maybe_transform(
                {
                    "task_name": task_name,
                    "url": url,
                    "audio_language": audio_language,
                    "client_entity_data": client_entity_data,
                    "client_user_id": client_user_id,
                    "subtitles_language": subtitles_language,
                    "category": category,
                    "stop_objects": stop_objects,
                },
                ai_task_create_params.AITaskCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AITaskCreateResponse,
        )

    def list(
        self,
        *,
        date_created: str | Omit = omit,
        limit: int | Omit = omit,
        ordering: Literal["task_id", "status", "task_name", "started_at"] | Omit = omit,
        page: int | Omit = omit,
        search: str | Omit = omit,
        status: Literal["FAILURE", "PENDING", "RECEIVED", "RETRY", "REVOKED", "STARTED", "SUCCESS"] | Omit = omit,
        task_id: str | Omit = omit,
        task_name: Literal["transcription", "content-moderation"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPageStreamingAI[AITask]:
        """
        Returns a list of previously created and processed AI tasks.

        The list contains brief information about the task and its execution status.
        Data is displayed page by page.

        Args:
          date_created: Time when task was created. Datetime in ISO 8601 format.

          limit: Number of results to return per page.

          ordering: Which field to use when ordering the results: `task_id`, status, and
              `task_name`. Sorting is done in ascending (ASC) order.

              If parameter is omitted then "started_at DESC" is used for ordering by default.

          page: Page to view from task list, starting from 1

          search: This is an field for combined text search in the following fields: `task_id`,
              `task_name`, status, and `task_data`.

              Both full and partial searches are possible inside specified above fields. For
              example, you can filter tasks of a certain category, or tasks by a specific
              original file.

              Example:

              - To filter tasks of Content Moderation NSFW method:
                `GET /streaming/ai/tasks?search=nsfw`
              - To filter tasks of processing video from a specific origin:
                `GET /streaming/ai/tasks?search=s3.eu-west-1.amazonaws.com`

          status: Task status

          task_id: The task unique identifier to find

          task_name: Type of the AI task. Reflects the original API method that was used to create
              the AI task.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/streaming/ai/tasks",
            page=SyncPageStreamingAI[AITask],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date_created": date_created,
                        "limit": limit,
                        "ordering": ordering,
                        "page": page,
                        "search": search,
                        "status": status,
                        "task_id": task_id,
                        "task_name": task_name,
                    },
                    ai_task_list_params.AITaskListParams,
                ),
            ),
            model=AITask,
        )

    def cancel(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AITaskCancelResponse:
        """
        Stopping a previously launched AI-task without waiting for it to be fully
        completed.

        The task will be moved to "REVOKED" status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return self._post(
            path_template("/streaming/ai/tasks/{task_id}/cancel", task_id=task_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AITaskCancelResponse,
        )

    def get(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AITaskGetResponse:
        """
        This is the single method to check the execution status of an AI task, and
        obtain the result of any type of AI task.

        Based on the results of processing, the “result” field will contain an answer
        corresponding to the type of the initially created task:

        - ASR: Transcribe video
        - ASR: Translate subtitles
        - CM: Sports detection
        - CM: Not Safe For Work (NSFW) content detection
        - CM: Soft nudity detection
        - CM: Hard nudity detection
        - CM: Objects recognition (soon)
        - etc... (see other methods from /ai/ domain)

        A queue is used to process videos. The waiting time depends on the total number
        of requests in the system, so sometimes you will have to wait.

        Statuses:

        - RECEIVED – the task is accepted by the system
        - PENDING – the task is received and it is pending for available resources
        - STARTED – processing has started
        - SUCCESS – processing has completed successfully
        - FAILURE – processing failed
        - REVOKED – processing was cancelled by the user (or the system)
        - RETRY – the task execution failed due to internal reasons, the task is queued
          for re-execution (up to 3 times)

        Each task is processed in sub-stages, for example, original language is first
        determined in a video, and then transcription is performed. In such cases, the
        video processing status may change from "STARTED" to "PENDING", and back. This
        is due to waiting for resources for a specific processing sub-stage. In this
        case, the overall percentage "progress" of video processing will reflect the
        full picture.

        The result data is stored for 1 month, after which it is deleted.

        For billing conditions see the corresponding methods in /ai/ domain. The task is
        billed only after successful completion of the task and transition to "SUCCESS"
        status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return self._get(
            path_template("/streaming/ai/tasks/{task_id}", task_id=task_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AITaskGetResponse,
        )

    def get_ai_settings(
        self,
        *,
        type: Literal["language_support"],
        audio_language: str | Omit = omit,
        subtitles_language: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AITaskGetAISettingsResponse:
        """
        The method for revealing basic information and advanced underlying settings that
        are used when performing AI-tasks.

        Parameter sections:

        - "language_support" – AI Translation: check if a language pair is supported or
          not for AI translation.
        - this list will expand as new AI methods are added.

        **`language_support`**

        There are many languages available for transcription. But not all languages can
        be automatically translated to and from with good quality. In order to determine
        the availability of translation from the audio language to the desired subtitle
        language, you can use this type of "language_support".

        AI models are constantly improving, so this method can be used for dynamic
        determination.

        Example:

        ```
        curl -L 'https://api.gcore.com/streaming/ai/info?type=language_support&audio_language=eng&subtitles_language=fre'

        { "supported": true }
        ```

        Today we provide the following capabilities as below.

        These are the 100 languages for which we support only transcription and
        translation to English. The iso639-2b codes for these are:
        `afr, sqi, amh, ara, hye, asm, aze, bak, eus, bel, ben, bos, bre, bul, mya, cat, zho, hrv, ces, dan, nld, eng, est, fao, fin, fra, glg, kat, deu, guj, hat, hau, haw, heb, hin, hun, isl, ind, ita, jpn, jav, kan, kaz, khm, kor, lao, lat, lav, lin, lit, ltz, mkd, mlg, msa, mal, mlt, mri, mar, ell, mon, nep, nor, nno, oci, pan, fas, pol, por, pus, ron, rus, san, srp, sna, snd, sin, slk, slv, som, spa, sun, swa, swe, tgl, tgk, tam, tat, tel, tha, bod, tur, tuk, ukr, urd, uzb, vie, cym, yid, yor`.

        These are the 77 languages for which we support translation to other languages
        and translation to:
        `afr, amh, ara, hye, asm, aze, eus, bel, ben, bos, bul, mya, cat, zho, hrv, ces, dan, nld, eng, est, fin, fra, glg, kat, deu, guj, heb, hin, hun, isl, ind, ita, jpn, jav, kan, kaz, khm, kor, lao, lav, lit, mkd, mal, mlt, mar, ell, mon, nep, nno, pan, fas, pol, por, pus, ron, rus, srp, sna, snd, slk, slv, som, spa, swa, swe, tgl, tgk, tam, tel, tha, tur, ukr, urd, vie, cym, yor`.

        Args:
          type: The parameters section for which parameters are requested

          audio_language: The source language from which the audio will be transcribed. Required when
              `type=language_support`. Value is 3-letter language code according to ISO-639-2
              (bibliographic code), (e.g., fre for French).

          subtitles_language: The target language the text will be translated into. If omitted, the API will
              return whether the `audio_language` is supported for transcription only, instead
              of translation. Value is 3-letter language code according to ISO-639-2
              (bibliographic code), (e.g., fre for French).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/streaming/ai/info",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "type": type,
                        "audio_language": audio_language,
                        "subtitles_language": subtitles_language,
                    },
                    ai_task_get_ai_settings_params.AITaskGetAISettingsParams,
                ),
            ),
            cast_to=AITaskGetAISettingsResponse,
        )


class AsyncAITasksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAITasksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAITasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAITasksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncAITasksResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        task_name: Literal["transcription"],
        url: str,
        audio_language: str | Omit = omit,
        client_entity_data: str | Omit = omit,
        client_user_id: str | Omit = omit,
        subtitles_language: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AITaskCreateResponse:
        """
        Creating an AI task.

        This method allows you to create an AI task for VOD video processing:

        - ASR: Transcribe video
        - ASR: Translate subtitles
        - CM: Sports detection
        - CM: Not Safe For Work (NSFW) content detection
        - CM: Soft nudity detection
        - CM: Hard nudity detection
        - CM: Objects recognition (soon)

        ![Auto generated subtitles example](https://demo-files.gvideo.io/apidocs/captions.gif)

        How to use:

        - Create an AI task, specify algorithm to use
        - Get `task_id`
        - Check a result using `.../ai/tasks/{task_id}` method

        For more detailed information, see the algorithm-specific sections below.

        **AI Automatic Speech Recognition (ASR)**

        AI is instrumental in automatic video processing for subtitles creation by using
        Automatic Speech Recognition (ASR) technology to transcribe spoken words into
        text, which can then be translated into multiple languages for broader
        accessibility.

        Categories:

        - `transcription` – to create subtitles/captions from audio in the original
          language.
        - `translation` – to translate subtitles/captions from the original language to
          99+ other languages.

        AI subtitle transcription and translation tools are highly efficient, processing
        large volumes of audio-visual content quickly and providing accurate
        transcriptions and translations with minimal human intervention. Additionally,
        AI-driven solutions can significantly reduce costs and turnaround times compared
        to traditional methods, making them an invaluable resource for content creators
        and broadcasters aiming to reach global audiences.

        Example response with positive result:

        ```
        {
          "status": "SUCCESS",
          "result": {
            "subtitles": [
              {
                  "start_time": "00:00:00.031",
                  "end_time": "00:00:03.831",
                  "text": "Come on team, ..."
              }, ...
            ]
            "vttContent": "WEBVTT\n\n1\n00:00:00.031 --> 00:00:03.831\nCome on team, ...",
            "concatenated_text": "Come on team, ...",
            "languages": [ "eng" ],
            "speech_detected": true
            }
          }, ...
        }
        ```

        **AI Content Moderation (CM)**

        The AI Content Moderation API offers a powerful solution for analyzing video
        content to detect various categories of inappropriate material. Leveraging
        state-of-the-art AI models, this API ensures real-time analysis and flagging of
        sensitive or restricted content types, making it an essential tool for platforms
        requiring stringent content moderation.

        Categories:

        - `nsfw`: Quick algorithm to detect pornographic material, ensuring content is
          "not-safe-for-work" or normal.
        - `hard_nudity`: Detailed analysis of video which detects explicit nudity
          involving genitalia.
        - `soft_nudity`: Detailed video analysis that reveals both explicit and partial
          nudity, including the presence of male and female faces and other uncovered
          body parts.
        - `sport`: Recognizes various sporting activities.

        The AI Content Moderation API is an invaluable tool for managing and controlling
        the type of content being shared or streamed on your platform. By implementing
        this API, you can ensure compliance with community guidelines and legal
        requirements, as well as provide a safer environment for your users.

        Important notes:

        - It's allowed to analyze still images too (where applicable). Format of image:
          JPEG, PNG. In that case one image is the same as video of 1 second duration.
        - Not all frames in the video are used for analysis, but only key frames
          (Iframe). For example, if a key frame in a video is set every ±2 seconds, then
          detection will only occur at these timestamps. If an object appears and
          disappears between these time stamps, it will not be detected. We are working
          on a version to analyze more frames, please contact your manager or our
          support team to enable this method.

        Example response with positive result:

        ```
        {
          "status": "SUCCESS",
          "result": {
              "nsfw_detected": true,
              "detection_results": [ "nsfw" ],
              "frames": [
                  {
                      "label": "nsfw",
                      "confidence": 1.0,
                      "frame_number": 24
                  },...
              ]
          }
        }
        ```

        **Additional information**

        Billing takes into account the duration of the analyzed video. Or the duration
        until the stop tag(where applicable), if the condition was triggered during the
        analysis.

        The heart of content moderation is AI, with additional services. They run on our
        own infrastructure, so the files/data are not transferred anywhere to external
        services. After processing, original files are also deleted from local storage
        of AI.

        Read more detailed information about our solution, and architecture, and
        benefits in the knowledge base and blog.

        **Algorithm-specific details**

        Create AI ASR task

        Transcribing is the process of writing down the words you hear in an audio. Our
        solution allows you to transcribe audio from your video and get subtitles
        automatically. To do this, we use modern AI models.

        The result:

        - Transcription – subtitles in the original language. I.e. audio is in English –
          subtitles are in English too, audio is in German – subtitles are in German
          too.
        - Translation – subtitles is translated from the original language to any other
          language.

        **How to use?**

        - Explicit call to this AI method. Applicable for any file stored with us or
          located on the Internet.
        - Standard video upload but with automatic subtitle generation. Look at
          ["VOD uploading"](/api-reference/streaming/videos/create-video).

        **What language will the subtitles be in?**

        You can specify the language explicitly, then it will be used to create
        subtitles: the source language in the audio, the resulting subtitle language. If
        this is not set, the system will run auto language identification and the
        subtitles will be in the detected language. The method also works based on AI
        analysis.

        Additionally, when this is not set, we also support recognition of alternate
        languages in the video (code-switching). For example, when in a video different
        speakers speak several languages, or when they switch from their native language
        to English and back. Thus when you have multiple languages in the video it is
        better to not specify an "audio_language" otherwise AI may force the system to
        recognize gibberish.

        **What can be transcribed?**

        Service uses additional methods to detect presence of speech in audio track,
        thus improving the detection of any human conversations:

        - Speech of one speaker,
        - Speech of several speakers,
        - Speech in different languages,
        - etc

        Restriction on music, lyrics most likely will not be created.

        **What about translation?**

        It is also possible to automatically translate from the original language to
        another you need.

        To create a translation, specify the desired language explicitly in
        "subtitles_language" parameter. Otherwise, the subtitles will be in the original
        language. Translation into different languages should be done by creating
        separate tasks.

        ![Auto generated subtitles example](https://demo-files.gvideo.io/apidocs/captions.gif)

        Use MP4 videos to process. This method is not tied to videos that are stored
        only in our video hosting (look at how get a link to MP4 rendition), so you can
        use links to any other external file with HTTP/HTTPS access.

        For now, only the first audio track can be processed; later this functionality
        will be improved to allow to use any. Also, not all language pairs are currently
        supported. If a language pair is not supported for automatic translation, the
        task status will be FAILURE with description of the reason. Example:
        `eng => uzb`. You can request to add the language pair you need for automatic
        translation. Contact our support.

        Example of modes to transcribe and/or translate:

        - Auto language detection: `{ "url":"..." }`
        - From German language explicitly : `{ "url":"...", "audio_language":"ger" }`
        - From any auto-detected to English language explicitly:
          `{ "url":"...", "subtitles_language":"eng" }`
        - From German language to English language explicitly:
          `{ "url":"...", "audio_language":"ger", "subtitles_language":"eng" }`

        Example of setting a task to process MP4 file (animated gif from above):

        ```
        curl -L 'https://api.gcore.com/streaming/ai/tasks' \\
        -H 'Content-Type: application/json' \\
        -H 'Authorization: APIKey 1234$abcd...' \\
        -d '{
            "url": "https://demo-files.gvideo.io/apidocs/spritefright-blender-cut30sec.mp4"
        }'
        ```

        As described above, transcription is done automatically using AI. Therefore, the
        quality may differ from a manual transcription by a professional person. If this
        happens to you, then you can download subtitles and change them in an external
        editor.

        Transcription and translation are 2 different AI tasks:

        - Transcription is set only for transcription.
        - Translation, if non-original languages are set for translation.

        Billing takes into account the duration of the analyzed original video.

        The heart for transcribing is the AI model Whisper from OpenAI, with additional
        optimizations and services. The AI models run on our own infrastructure, so the
        files/data are not transferred anywhere to external services. After processing,
        original files are also deleted from local storage of AI.

        Read more detailed information about our solution, and architecture, and
        benefits in the knowledge base and blog.

        Create AI CM:nsfw task

        This algorithm allows to quickly detect inappropriate content, determining that
        the content is NSFW ("Not Safe For Work") or normal. Generic info about all
        capabilities and limits see in the generic
        ["Content Moderation"](/api-reference/streaming/ai/create-ai-task) method.

        **What is "Not Safe For Work"?**

        The algorithm has recognized inappropriate content in a video and it might not
        be suitable to view in public places. The solution provides its confidence level
        (in percentage) of how sure it is that the content is NSFW, or it most likely
        does not contain any sexual or similar content.

        Different to soft-nudity-detection and hard-nudity-detection, this model will
        only check for sensitive material that can be considered not-safe-for-work.

        ![AI Content Moderation: NSFW detection visual example](https://demo-files.gvideo.io/apidocs/nsfw-detection.gif)

        **How to use?**

        Frames within the specified video are analyzed.

        Response will contain only frames for which the class nsfw is detected with a
        confidence of more than 50%.

        Example of detected NSFW:

        ```
        {
          "nsfw_detected": true,
          "detection_results": [ "nsfw" ],
          "frames": [
              {
                  "label": "nsfw",
                  "confidence": 0.93,
                  "frame_number": 1
              },..
          ]
        }
        ```

        Example of a response without detecting inappropriate content:

        ```
        {
          "nsfw_detected": false,
          "detection_results": [],
          "frames": []
        }
        ```

        Please note that the API only provides a set of data (json) about the objects
        found, so no video is generated. The demo video video (above ^) was specially
        created based on json from the API for visual demonstration and better
        perception of the possibilities.

        Create AI CM:`hard_nudity` task

        This algorithm allows to detect explicit nudity of the human body (involving
        genitals) in a video. Generic info about all capabilities and limits see in the
        generic ["Content Moderation"](/api-reference/streaming/ai/create-ai-task)
        method.

        **What is Hard nudity detection?**

        This method is often used to analyze UGC to determine whether videos can be
        published to all users, or to prohibit publication due to offensive and
        inappropriate content.

        Objects that can be detected:

        - `ANUS_EXPOSED`
        - `BUTTOCKS_EXPOSED`
        - `FEMALE_BREAST_EXPOSED`
        - `FEMALE_GENITALIA_EXPOSED`
        - `MALE_BREAST_EXPOSED`
        - `MALE_GENITALIA_EXPOSED`

        Please note that the number of objects is less than in the
        soft-nudity-detection. This method works faster and better if only exposed body
        parts detection is required.

        ![AI Content Moderation: hard nudity detection visual example](https://demo-files.gvideo.io/apidocs/nudity_detection.gif)

        **How to use?**

        The information is returned with the video frame number where it was found and
        probability of the detected object. Nudity detection is done using AI, so for
        each object a probability percentage is applied; objects with a probability of
        at least 30% are included in the response.

        Video processing speed is approximately 1:5.

        Example of detected nudity or body parts:

        ```
        {
          "nudity_detected": true,
          "detection_results": [ "MALE_GENITALIA_EXPOSED" ]
          "frames": [
              {
                  "confidence": 0.75,
                  "frame_number": 35,
                  "label": "MALE_GENITALIA_EXPOSED"
              },...
          ]
        }
        ```

        Example response when nudity or body parts were not found:

        ```
        {
          "nudity_detected": false,
          "detection_results": []
          "frames": []
        }
        ```

        There is no universal recipe under which a video can be considered unacceptable,
        since different services host different types of videos for different audiences:
        adult content, children's content, educational content, etc. You can determine
        the probability threshold at which you consider a video inappropriate. The
        easiest option is to run several of your videos and analyze the resulting
        probability coefficient.

        Sometimes a detected object at the beginning of the video immediately makes it
        clear that there is no need to further analyze the video. For such cases, you
        can use stop tags. Use parameter "stop_objects" to specify comma separated stop
        tags. It is also possible to specify % probability threshold value, above which
        the stop tag will be triggered.

        ```
          {
              "url": "...",
              "stop_objects": "MALE_GENITALIA_EXPOSED:0.8,FEMALE_GENITALIA_EXPOSED"
          }
        ```

        Please note that the API only provides a set of data (json) about the objects
        found, so no video is generated. The demo video video (above ^) was specially
        created based on json from the API for visual demonstration and better
        perception of the possibilities.

        Create AI CM:`soft_nudity` task

        This algorithm allows to identify explicit nudity and partial nudity too
        (including the presence of male and female faces and other uncovered body parts)
        in a video. Generic info about all capabilities and limits see in the generic
        ["Content Moderation"](/api-reference/streaming/ai/create-ai-task) method.

        **What is Soft nudity detection?**

        This method is often used to analyze UGC to determine whether videos can be
        published to all users, or to prohibit publication due to offensive and
        inappropriate content.

        Objects that can be detected:

        - `ANUS_COVERED`
        - `ANUS_EXPOSED`
        - `ARMPITS_COVERED`
        - `ARMPITS_EXPOSED`
        - `BELLY_COVERED`
        - `BELLY_EXPOSED`
        - `BUTTOCKS_COVERED`
        - `BUTTOCKS_EXPOSED`
        - `FACE_FEMALE`
        - `FACE_MALE`
        - `FEET_COVERED`
        - `FEET_EXPOSED`
        - `FEMALE_BREAST_COVERED`
        - `FEMALE_BREAST_EXPOSED`
        - `FEMALE_GENITALIA_COVERED`
        - `FEMALE_GENITALIA_EXPOSED`
        - `MALE_BREAST_EXPOSED`
        - `MALE_GENITALIA_EXPOSED`

        This method allows you to identify faces and other body parts. Used to find
        complex combinations of what is happening in a video. Please note that the
        number of objects is more than in the hard-nudity-detection. The method is
        slower.

        ![AI Content Moderation: hard nudity detection visual example](https://demo-files.gvideo.io/apidocs/soft_nudity_detection.gif)

        **How to use?**

        The information is returned with the video frame number where it was found and
        probability of the detected object. Nudity detection is done using AI, so for
        each object a probability percentage is applied; objects with a probability of
        at least 30% are included in the response.

        Video processing speed is approximately 1:5.

        Example of detected nudity or body parts:

        ```
        {
          "nudity_detected": true,
          "detection_results": [ "FACE_FEMALE", "BELLY_COVERED" ]
          "frames": [
              {
                  "confidence": 0.82,
                  "frame_number": 1,
                  "label": "BELLY_COVERED"
              },...
          ]
        }
        ```

        Example response when nudity or body parts were not found:

        ```
        {
          "nudity_detected": false,
          "detection_results": []
          "frames": []
        }
        ```

        There is no universal recipe under which a video can be considered unacceptable,
        since different services host different types of videos for different audiences:
        adult content, children's content, educational content, etc. You can determine
        the probability threshold at which you consider a video inappropriate. The
        easiest option is to run several of your videos and analyze the resulting
        probability coefficient.

        Sometimes a detected object at the beginning of the video immediately makes it
        clear that there is no need to further analyze the video. For such cases, you
        can use stop tags. Use parameter "stop_objects" to specify comma separated stop
        tags. It is also possible to specify % probability threshold value, above which
        the stop tag will be triggered.

        ```
          {
              "url": "...",
              "stop_objects": "BELLY_COVERED:0.9,FEMALE_GENITALIA_COVERED"
          }
        ```

        Please note that the API only provides a set of data (json) about the objects
        found, so no video is generated. The demo video video (above ^) was specially
        created based on json from the API for visual demonstration and better
        perception of the possibilities.

        Create AI CM:sport task

        This algorithm allows to identify various sporting activities in a video.
        Generic info about all capabilities and limits see in the generic
        ["Content Moderation"](/api-reference/streaming/ai/create-ai-task) method.

        **What is Sports activity detection?**

        Sports activity detection by AI involves using machine learning and computer
        vision technologies to automatically identify, analyze, and interpret various
        activities within sports and generic videos. This can include detecting specific
        types, actions, events, and moments.

        This model operates on a video sequence (and not on images as most of the used
        computer vision models). Make sure your video is at least 10-15 seconds long.

        Sports activities can be detected:

        - archery
        - arm wrestling
        - playing badminton
        - playing baseball
        - basketball dunk
        - bowling
        - boxing punch
        - boxing speed bag
        - catching or throwing baseball
        - catching or throwing softball
        - cricket
        - curling
        - disc golfing
        - dodgeball
        - fencing
        - football
        - golf chipping
        - golf driving
        - golf putting
        - hitting baseball
        - hockey stop
        - ice skating
        - javelin throw
        - juggling soccer ball
        - kayaking
        - kicking field goal
        - kicking soccer ball
        - playing cricket
        - playing field hockey
        - playing ice hockey
        - playing kickball
        - playing lacrosse
        - playing ping pong
        - playing polo
        - playing squash or racquetball
        - playing tennis
        - playing volleyball
        - pole vault
        - riding a bike
        - riding or walking with horse
        - roller skating
        - rowing
        - sailing
        - shooting goal (soccer)
        - skateboarding
        - skiing

        Use cases:

        - Sports leagues and content creators can use AI to monitor UGC for unauthorized
          publications of their content. This can include detecting specific sporting
          events or activities that are part of copyrighted content.
        - Sports fans often miss live games and rely on highlight reels. AI can
          automatically detect key moments like goals, touchdowns, or game-winning shots
          in uploaded UGC videos and compile them into personalized highlight reels.

        ![AI Content Moderation: sports activity detection visual example](https://demo-files.gvideo.io/apidocs/sports_football_detection.gif)

        **How to use?**

        The information is returned with the video frame number where it was found and
        probability of the detected activity. Identification is done using AI, so for
        each activity a probability percentage is applied; activities with a probability
        of at least 30% are included in the response.

        Video processing speed is approximately 1:5.

        Example of detected sports activity:

        ```
        {
          "sport_detected": true,
          "detection_results": [ "shooting goal (soccer)" ],
          "frames": [
              {
                  "label": "shooting goal (soccer)",
                  "frame_number": 98,
                  "confidence": 0.99
              },...
          ]
        }
        ```

        Example response when sports activities were not found:

        ```
        {
          "sport_detected": false,
          "detection_results": []
          "frames": []
        }
        ```

        Please note that the API only provides a set of data (json) about the objects
        found, so no video is generated. The demo video video (above ^) was specially
        created based on json from the API for visual demonstration and better
        perception of the possibilities.

        Args:
          task_name: Name of the task to be performed

          url: URL to the MP4 file to analyze. File must be publicly accessible via HTTP/HTTPS.

          audio_language: Language in original audio (transcription only). This value is used to determine
              the language from which to transcribe.

              If this is not set, the system will run auto language identification and the
              subtitles will be in the detected language. The method also works based on AI
              analysis. It's fairly accurate, but if it's wrong, then set the language
              explicitly.

              Additionally, when this is not set, we also support recognition of alternate
              languages in the video (language code-switching).

              Language is set by 3-letter language code according to ISO-639-2 (bibliographic
              code).

              We can process languages:

              - 'afr': Afrikaans
              - 'alb': Albanian
              - 'amh': Amharic
              - 'ara': Arabic
              - 'arm': Armenian
              - 'asm': Assamese
              - 'aze': Azerbaijani
              - 'bak': Bashkir
              - 'baq': Basque
              - 'bel': Belarusian
              - 'ben': Bengali
              - 'bos': Bosnian
              - 'bre': Breton
              - 'bul': Bulgarian
              - 'bur': Myanmar
              - 'cat': Catalan
              - 'chi': Chinese
              - 'cze': Czech
              - 'dan': Danish
              - 'dut': Nynorsk
              - 'eng': English
              - 'est': Estonian
              - 'fao': Faroese
              - 'fin': Finnish
              - 'fre': French
              - 'geo': Georgian
              - 'ger': German
              - 'glg': Galician
              - 'gre': Greek
              - 'guj': Gujarati
              - 'hat': Haitian creole
              - 'hau': Hausa
              - 'haw': Hawaiian
              - 'heb': Hebrew
              - 'hin': Hindi
              - 'hrv': Croatian
              - 'hun': Hungarian
              - 'ice': Icelandic
              - 'ind': Indonesian
              - 'ita': Italian
              - 'jav': Javanese
              - 'jpn': Japanese
              - 'kan': Kannada
              - 'kaz': Kazakh
              - 'khm': Khmer
              - 'kor': Korean
              - 'lao': Lao
              - 'lat': Latin
              - 'lav': Latvian
              - 'lin': Lingala
              - 'lit': Lithuanian
              - 'ltz': Luxembourgish
              - 'mac': Macedonian
              - 'mal': Malayalam
              - 'mao': Maori
              - 'mar': Marathi
              - 'may': Malay
              - 'mlg': Malagasy
              - 'mlt': Maltese
              - 'mon': Mongolian
              - 'nep': Nepali
              - 'dut': Dutch
              - 'nor': Norwegian
              - 'oci': Occitan
              - 'pan': Punjabi
              - 'per': Persian
              - 'pol': Polish
              - 'por': Portuguese
              - 'pus': Pashto
              - 'rum': Romanian
              - 'rus': Russian
              - 'san': Sanskrit
              - 'sin': Sinhala
              - 'slo': Slovak
              - 'slv': Slovenian
              - 'sna': Shona
              - 'snd': Sindhi
              - 'som': Somali
              - 'spa': Spanish
              - 'srp': Serbian
              - 'sun': Sundanese
              - 'swa': Swahili
              - 'swe': Swedish
              - 'tam': Tamil
              - 'tat': Tatar
              - 'tel': Telugu
              - 'tgk': Tajik
              - 'tgl': Tagalog
              - 'tha': Thai
              - 'tib': Tibetan
              - 'tuk': Turkmen
              - 'tur': Turkish
              - 'ukr': Ukrainian
              - 'urd': Urdu
              - 'uzb': Uzbek
              - 'vie': Vietnamese
              - 'wel': Welsh
              - 'yid': Yiddish
              - 'yor': Yoruba

          client_entity_data: Meta parameter, designed to store your own extra information about a video
              entity: video source, video id, etc. It is not used in any way in video
              processing.

              For example, if an AI-task was created automatically when you uploaded a video
              with the AI auto-processing option (transcribing, translation), then the ID of
              the associated video for which the task was performed will be explicitly
              indicated here.

          client_user_id: Meta parameter, designed to store your own identifier. Can be used by you to tag
              requests from different end-users. It is not used in any way in video
              processing.

          subtitles_language: Indicates which language it is clearly necessary to translate into. If this is
              not set, the original language will be used from attribute "audio_language".

              Please note that:

              - transcription into the original language is a free procedure,
              - and translation from the original language into any other languages is a
                "translation" procedure and is paid. More details in
                [POST /streaming/ai/tasks](/api-reference/streaming/ai/create-ai-task).
                Language is set by 3-letter language code according to ISO-639-2
                (bibliographic code).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        category: Literal["nsfw"],
        task_name: Literal["content-moderation"],
        url: str,
        client_entity_data: str | Omit = omit,
        client_user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AITaskCreateResponse:
        """
        Creating an AI task.

        This method allows you to create an AI task for VOD video processing:

        - ASR: Transcribe video
        - ASR: Translate subtitles
        - CM: Sports detection
        - CM: Not Safe For Work (NSFW) content detection
        - CM: Soft nudity detection
        - CM: Hard nudity detection
        - CM: Objects recognition (soon)

        ![Auto generated subtitles example](https://demo-files.gvideo.io/apidocs/captions.gif)

        How to use:

        - Create an AI task, specify algorithm to use
        - Get `task_id`
        - Check a result using `.../ai/tasks/{task_id}` method

        For more detailed information, see the algorithm-specific sections below.

        **AI Automatic Speech Recognition (ASR)**

        AI is instrumental in automatic video processing for subtitles creation by using
        Automatic Speech Recognition (ASR) technology to transcribe spoken words into
        text, which can then be translated into multiple languages for broader
        accessibility.

        Categories:

        - `transcription` – to create subtitles/captions from audio in the original
          language.
        - `translation` – to translate subtitles/captions from the original language to
          99+ other languages.

        AI subtitle transcription and translation tools are highly efficient, processing
        large volumes of audio-visual content quickly and providing accurate
        transcriptions and translations with minimal human intervention. Additionally,
        AI-driven solutions can significantly reduce costs and turnaround times compared
        to traditional methods, making them an invaluable resource for content creators
        and broadcasters aiming to reach global audiences.

        Example response with positive result:

        ```
        {
          "status": "SUCCESS",
          "result": {
            "subtitles": [
              {
                  "start_time": "00:00:00.031",
                  "end_time": "00:00:03.831",
                  "text": "Come on team, ..."
              }, ...
            ]
            "vttContent": "WEBVTT\n\n1\n00:00:00.031 --> 00:00:03.831\nCome on team, ...",
            "concatenated_text": "Come on team, ...",
            "languages": [ "eng" ],
            "speech_detected": true
            }
          }, ...
        }
        ```

        **AI Content Moderation (CM)**

        The AI Content Moderation API offers a powerful solution for analyzing video
        content to detect various categories of inappropriate material. Leveraging
        state-of-the-art AI models, this API ensures real-time analysis and flagging of
        sensitive or restricted content types, making it an essential tool for platforms
        requiring stringent content moderation.

        Categories:

        - `nsfw`: Quick algorithm to detect pornographic material, ensuring content is
          "not-safe-for-work" or normal.
        - `hard_nudity`: Detailed analysis of video which detects explicit nudity
          involving genitalia.
        - `soft_nudity`: Detailed video analysis that reveals both explicit and partial
          nudity, including the presence of male and female faces and other uncovered
          body parts.
        - `sport`: Recognizes various sporting activities.

        The AI Content Moderation API is an invaluable tool for managing and controlling
        the type of content being shared or streamed on your platform. By implementing
        this API, you can ensure compliance with community guidelines and legal
        requirements, as well as provide a safer environment for your users.

        Important notes:

        - It's allowed to analyze still images too (where applicable). Format of image:
          JPEG, PNG. In that case one image is the same as video of 1 second duration.
        - Not all frames in the video are used for analysis, but only key frames
          (Iframe). For example, if a key frame in a video is set every ±2 seconds, then
          detection will only occur at these timestamps. If an object appears and
          disappears between these time stamps, it will not be detected. We are working
          on a version to analyze more frames, please contact your manager or our
          support team to enable this method.

        Example response with positive result:

        ```
        {
          "status": "SUCCESS",
          "result": {
              "nsfw_detected": true,
              "detection_results": [ "nsfw" ],
              "frames": [
                  {
                      "label": "nsfw",
                      "confidence": 1.0,
                      "frame_number": 24
                  },...
              ]
          }
        }
        ```

        **Additional information**

        Billing takes into account the duration of the analyzed video. Or the duration
        until the stop tag(where applicable), if the condition was triggered during the
        analysis.

        The heart of content moderation is AI, with additional services. They run on our
        own infrastructure, so the files/data are not transferred anywhere to external
        services. After processing, original files are also deleted from local storage
        of AI.

        Read more detailed information about our solution, and architecture, and
        benefits in the knowledge base and blog.

        **Algorithm-specific details**

        Create AI ASR task

        Transcribing is the process of writing down the words you hear in an audio. Our
        solution allows you to transcribe audio from your video and get subtitles
        automatically. To do this, we use modern AI models.

        The result:

        - Transcription – subtitles in the original language. I.e. audio is in English –
          subtitles are in English too, audio is in German – subtitles are in German
          too.
        - Translation – subtitles is translated from the original language to any other
          language.

        **How to use?**

        - Explicit call to this AI method. Applicable for any file stored with us or
          located on the Internet.
        - Standard video upload but with automatic subtitle generation. Look at
          ["VOD uploading"](/api-reference/streaming/videos/create-video).

        **What language will the subtitles be in?**

        You can specify the language explicitly, then it will be used to create
        subtitles: the source language in the audio, the resulting subtitle language. If
        this is not set, the system will run auto language identification and the
        subtitles will be in the detected language. The method also works based on AI
        analysis.

        Additionally, when this is not set, we also support recognition of alternate
        languages in the video (code-switching). For example, when in a video different
        speakers speak several languages, or when they switch from their native language
        to English and back. Thus when you have multiple languages in the video it is
        better to not specify an "audio_language" otherwise AI may force the system to
        recognize gibberish.

        **What can be transcribed?**

        Service uses additional methods to detect presence of speech in audio track,
        thus improving the detection of any human conversations:

        - Speech of one speaker,
        - Speech of several speakers,
        - Speech in different languages,
        - etc

        Restriction on music, lyrics most likely will not be created.

        **What about translation?**

        It is also possible to automatically translate from the original language to
        another you need.

        To create a translation, specify the desired language explicitly in
        "subtitles_language" parameter. Otherwise, the subtitles will be in the original
        language. Translation into different languages should be done by creating
        separate tasks.

        ![Auto generated subtitles example](https://demo-files.gvideo.io/apidocs/captions.gif)

        Use MP4 videos to process. This method is not tied to videos that are stored
        only in our video hosting (look at how get a link to MP4 rendition), so you can
        use links to any other external file with HTTP/HTTPS access.

        For now, only the first audio track can be processed; later this functionality
        will be improved to allow to use any. Also, not all language pairs are currently
        supported. If a language pair is not supported for automatic translation, the
        task status will be FAILURE with description of the reason. Example:
        `eng => uzb`. You can request to add the language pair you need for automatic
        translation. Contact our support.

        Example of modes to transcribe and/or translate:

        - Auto language detection: `{ "url":"..." }`
        - From German language explicitly : `{ "url":"...", "audio_language":"ger" }`
        - From any auto-detected to English language explicitly:
          `{ "url":"...", "subtitles_language":"eng" }`
        - From German language to English language explicitly:
          `{ "url":"...", "audio_language":"ger", "subtitles_language":"eng" }`

        Example of setting a task to process MP4 file (animated gif from above):

        ```
        curl -L 'https://api.gcore.com/streaming/ai/tasks' \\
        -H 'Content-Type: application/json' \\
        -H 'Authorization: APIKey 1234$abcd...' \\
        -d '{
            "url": "https://demo-files.gvideo.io/apidocs/spritefright-blender-cut30sec.mp4"
        }'
        ```

        As described above, transcription is done automatically using AI. Therefore, the
        quality may differ from a manual transcription by a professional person. If this
        happens to you, then you can download subtitles and change them in an external
        editor.

        Transcription and translation are 2 different AI tasks:

        - Transcription is set only for transcription.
        - Translation, if non-original languages are set for translation.

        Billing takes into account the duration of the analyzed original video.

        The heart for transcribing is the AI model Whisper from OpenAI, with additional
        optimizations and services. The AI models run on our own infrastructure, so the
        files/data are not transferred anywhere to external services. After processing,
        original files are also deleted from local storage of AI.

        Read more detailed information about our solution, and architecture, and
        benefits in the knowledge base and blog.

        Create AI CM:nsfw task

        This algorithm allows to quickly detect inappropriate content, determining that
        the content is NSFW ("Not Safe For Work") or normal. Generic info about all
        capabilities and limits see in the generic
        ["Content Moderation"](/api-reference/streaming/ai/create-ai-task) method.

        **What is "Not Safe For Work"?**

        The algorithm has recognized inappropriate content in a video and it might not
        be suitable to view in public places. The solution provides its confidence level
        (in percentage) of how sure it is that the content is NSFW, or it most likely
        does not contain any sexual or similar content.

        Different to soft-nudity-detection and hard-nudity-detection, this model will
        only check for sensitive material that can be considered not-safe-for-work.

        ![AI Content Moderation: NSFW detection visual example](https://demo-files.gvideo.io/apidocs/nsfw-detection.gif)

        **How to use?**

        Frames within the specified video are analyzed.

        Response will contain only frames for which the class nsfw is detected with a
        confidence of more than 50%.

        Example of detected NSFW:

        ```
        {
          "nsfw_detected": true,
          "detection_results": [ "nsfw" ],
          "frames": [
              {
                  "label": "nsfw",
                  "confidence": 0.93,
                  "frame_number": 1
              },..
          ]
        }
        ```

        Example of a response without detecting inappropriate content:

        ```
        {
          "nsfw_detected": false,
          "detection_results": [],
          "frames": []
        }
        ```

        Please note that the API only provides a set of data (json) about the objects
        found, so no video is generated. The demo video video (above ^) was specially
        created based on json from the API for visual demonstration and better
        perception of the possibilities.

        Create AI CM:`hard_nudity` task

        This algorithm allows to detect explicit nudity of the human body (involving
        genitals) in a video. Generic info about all capabilities and limits see in the
        generic ["Content Moderation"](/api-reference/streaming/ai/create-ai-task)
        method.

        **What is Hard nudity detection?**

        This method is often used to analyze UGC to determine whether videos can be
        published to all users, or to prohibit publication due to offensive and
        inappropriate content.

        Objects that can be detected:

        - `ANUS_EXPOSED`
        - `BUTTOCKS_EXPOSED`
        - `FEMALE_BREAST_EXPOSED`
        - `FEMALE_GENITALIA_EXPOSED`
        - `MALE_BREAST_EXPOSED`
        - `MALE_GENITALIA_EXPOSED`

        Please note that the number of objects is less than in the
        soft-nudity-detection. This method works faster and better if only exposed body
        parts detection is required.

        ![AI Content Moderation: hard nudity detection visual example](https://demo-files.gvideo.io/apidocs/nudity_detection.gif)

        **How to use?**

        The information is returned with the video frame number where it was found and
        probability of the detected object. Nudity detection is done using AI, so for
        each object a probability percentage is applied; objects with a probability of
        at least 30% are included in the response.

        Video processing speed is approximately 1:5.

        Example of detected nudity or body parts:

        ```
        {
          "nudity_detected": true,
          "detection_results": [ "MALE_GENITALIA_EXPOSED" ]
          "frames": [
              {
                  "confidence": 0.75,
                  "frame_number": 35,
                  "label": "MALE_GENITALIA_EXPOSED"
              },...
          ]
        }
        ```

        Example response when nudity or body parts were not found:

        ```
        {
          "nudity_detected": false,
          "detection_results": []
          "frames": []
        }
        ```

        There is no universal recipe under which a video can be considered unacceptable,
        since different services host different types of videos for different audiences:
        adult content, children's content, educational content, etc. You can determine
        the probability threshold at which you consider a video inappropriate. The
        easiest option is to run several of your videos and analyze the resulting
        probability coefficient.

        Sometimes a detected object at the beginning of the video immediately makes it
        clear that there is no need to further analyze the video. For such cases, you
        can use stop tags. Use parameter "stop_objects" to specify comma separated stop
        tags. It is also possible to specify % probability threshold value, above which
        the stop tag will be triggered.

        ```
          {
              "url": "...",
              "stop_objects": "MALE_GENITALIA_EXPOSED:0.8,FEMALE_GENITALIA_EXPOSED"
          }
        ```

        Please note that the API only provides a set of data (json) about the objects
        found, so no video is generated. The demo video video (above ^) was specially
        created based on json from the API for visual demonstration and better
        perception of the possibilities.

        Create AI CM:`soft_nudity` task

        This algorithm allows to identify explicit nudity and partial nudity too
        (including the presence of male and female faces and other uncovered body parts)
        in a video. Generic info about all capabilities and limits see in the generic
        ["Content Moderation"](/api-reference/streaming/ai/create-ai-task) method.

        **What is Soft nudity detection?**

        This method is often used to analyze UGC to determine whether videos can be
        published to all users, or to prohibit publication due to offensive and
        inappropriate content.

        Objects that can be detected:

        - `ANUS_COVERED`
        - `ANUS_EXPOSED`
        - `ARMPITS_COVERED`
        - `ARMPITS_EXPOSED`
        - `BELLY_COVERED`
        - `BELLY_EXPOSED`
        - `BUTTOCKS_COVERED`
        - `BUTTOCKS_EXPOSED`
        - `FACE_FEMALE`
        - `FACE_MALE`
        - `FEET_COVERED`
        - `FEET_EXPOSED`
        - `FEMALE_BREAST_COVERED`
        - `FEMALE_BREAST_EXPOSED`
        - `FEMALE_GENITALIA_COVERED`
        - `FEMALE_GENITALIA_EXPOSED`
        - `MALE_BREAST_EXPOSED`
        - `MALE_GENITALIA_EXPOSED`

        This method allows you to identify faces and other body parts. Used to find
        complex combinations of what is happening in a video. Please note that the
        number of objects is more than in the hard-nudity-detection. The method is
        slower.

        ![AI Content Moderation: hard nudity detection visual example](https://demo-files.gvideo.io/apidocs/soft_nudity_detection.gif)

        **How to use?**

        The information is returned with the video frame number where it was found and
        probability of the detected object. Nudity detection is done using AI, so for
        each object a probability percentage is applied; objects with a probability of
        at least 30% are included in the response.

        Video processing speed is approximately 1:5.

        Example of detected nudity or body parts:

        ```
        {
          "nudity_detected": true,
          "detection_results": [ "FACE_FEMALE", "BELLY_COVERED" ]
          "frames": [
              {
                  "confidence": 0.82,
                  "frame_number": 1,
                  "label": "BELLY_COVERED"
              },...
          ]
        }
        ```

        Example response when nudity or body parts were not found:

        ```
        {
          "nudity_detected": false,
          "detection_results": []
          "frames": []
        }
        ```

        There is no universal recipe under which a video can be considered unacceptable,
        since different services host different types of videos for different audiences:
        adult content, children's content, educational content, etc. You can determine
        the probability threshold at which you consider a video inappropriate. The
        easiest option is to run several of your videos and analyze the resulting
        probability coefficient.

        Sometimes a detected object at the beginning of the video immediately makes it
        clear that there is no need to further analyze the video. For such cases, you
        can use stop tags. Use parameter "stop_objects" to specify comma separated stop
        tags. It is also possible to specify % probability threshold value, above which
        the stop tag will be triggered.

        ```
          {
              "url": "...",
              "stop_objects": "BELLY_COVERED:0.9,FEMALE_GENITALIA_COVERED"
          }
        ```

        Please note that the API only provides a set of data (json) about the objects
        found, so no video is generated. The demo video video (above ^) was specially
        created based on json from the API for visual demonstration and better
        perception of the possibilities.

        Create AI CM:sport task

        This algorithm allows to identify various sporting activities in a video.
        Generic info about all capabilities and limits see in the generic
        ["Content Moderation"](/api-reference/streaming/ai/create-ai-task) method.

        **What is Sports activity detection?**

        Sports activity detection by AI involves using machine learning and computer
        vision technologies to automatically identify, analyze, and interpret various
        activities within sports and generic videos. This can include detecting specific
        types, actions, events, and moments.

        This model operates on a video sequence (and not on images as most of the used
        computer vision models). Make sure your video is at least 10-15 seconds long.

        Sports activities can be detected:

        - archery
        - arm wrestling
        - playing badminton
        - playing baseball
        - basketball dunk
        - bowling
        - boxing punch
        - boxing speed bag
        - catching or throwing baseball
        - catching or throwing softball
        - cricket
        - curling
        - disc golfing
        - dodgeball
        - fencing
        - football
        - golf chipping
        - golf driving
        - golf putting
        - hitting baseball
        - hockey stop
        - ice skating
        - javelin throw
        - juggling soccer ball
        - kayaking
        - kicking field goal
        - kicking soccer ball
        - playing cricket
        - playing field hockey
        - playing ice hockey
        - playing kickball
        - playing lacrosse
        - playing ping pong
        - playing polo
        - playing squash or racquetball
        - playing tennis
        - playing volleyball
        - pole vault
        - riding a bike
        - riding or walking with horse
        - roller skating
        - rowing
        - sailing
        - shooting goal (soccer)
        - skateboarding
        - skiing

        Use cases:

        - Sports leagues and content creators can use AI to monitor UGC for unauthorized
          publications of their content. This can include detecting specific sporting
          events or activities that are part of copyrighted content.
        - Sports fans often miss live games and rely on highlight reels. AI can
          automatically detect key moments like goals, touchdowns, or game-winning shots
          in uploaded UGC videos and compile them into personalized highlight reels.

        ![AI Content Moderation: sports activity detection visual example](https://demo-files.gvideo.io/apidocs/sports_football_detection.gif)

        **How to use?**

        The information is returned with the video frame number where it was found and
        probability of the detected activity. Identification is done using AI, so for
        each activity a probability percentage is applied; activities with a probability
        of at least 30% are included in the response.

        Video processing speed is approximately 1:5.

        Example of detected sports activity:

        ```
        {
          "sport_detected": true,
          "detection_results": [ "shooting goal (soccer)" ],
          "frames": [
              {
                  "label": "shooting goal (soccer)",
                  "frame_number": 98,
                  "confidence": 0.99
              },...
          ]
        }
        ```

        Example response when sports activities were not found:

        ```
        {
          "sport_detected": false,
          "detection_results": []
          "frames": []
        }
        ```

        Please note that the API only provides a set of data (json) about the objects
        found, so no video is generated. The demo video video (above ^) was specially
        created based on json from the API for visual demonstration and better
        perception of the possibilities.

        Args:
          category: AI content moderation with NSFW detection algorithm

          task_name: Name of the task to be performed

          url: URL to the MP4 file to analyze. File must be publicly accessible via HTTP/HTTPS.

          client_entity_data: Meta parameter, designed to store your own extra information about a video
              entity: video source, video id, etc. It is not used in any way in video
              processing.

              For example, if an AI-task was created automatically when you uploaded a video
              with the AI auto-processing option (nudity detection, etc), then the ID of the
              associated video for which the task was performed will be explicitly indicated
              here.

          client_user_id: Meta parameter, designed to store your own identifier. Can be used by you to tag
              requests from different end-users. It is not used in any way in video
              processing.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        category: Literal["hard_nudity"],
        task_name: Literal["content-moderation"],
        url: str,
        client_entity_data: str | Omit = omit,
        client_user_id: str | Omit = omit,
        stop_objects: Literal[
            "ANUS_EXPOSED",
            "BUTTOCKS_EXPOSED",
            "FEMALE_BREAST_EXPOSED",
            "FEMALE_GENITALIA_EXPOSED",
            "MALE_BREAST_EXPOSED",
            "MALE_GENITALIA_EXPOSED",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AITaskCreateResponse:
        """
        Creating an AI task.

        This method allows you to create an AI task for VOD video processing:

        - ASR: Transcribe video
        - ASR: Translate subtitles
        - CM: Sports detection
        - CM: Not Safe For Work (NSFW) content detection
        - CM: Soft nudity detection
        - CM: Hard nudity detection
        - CM: Objects recognition (soon)

        ![Auto generated subtitles example](https://demo-files.gvideo.io/apidocs/captions.gif)

        How to use:

        - Create an AI task, specify algorithm to use
        - Get `task_id`
        - Check a result using `.../ai/tasks/{task_id}` method

        For more detailed information, see the algorithm-specific sections below.

        **AI Automatic Speech Recognition (ASR)**

        AI is instrumental in automatic video processing for subtitles creation by using
        Automatic Speech Recognition (ASR) technology to transcribe spoken words into
        text, which can then be translated into multiple languages for broader
        accessibility.

        Categories:

        - `transcription` – to create subtitles/captions from audio in the original
          language.
        - `translation` – to translate subtitles/captions from the original language to
          99+ other languages.

        AI subtitle transcription and translation tools are highly efficient, processing
        large volumes of audio-visual content quickly and providing accurate
        transcriptions and translations with minimal human intervention. Additionally,
        AI-driven solutions can significantly reduce costs and turnaround times compared
        to traditional methods, making them an invaluable resource for content creators
        and broadcasters aiming to reach global audiences.

        Example response with positive result:

        ```
        {
          "status": "SUCCESS",
          "result": {
            "subtitles": [
              {
                  "start_time": "00:00:00.031",
                  "end_time": "00:00:03.831",
                  "text": "Come on team, ..."
              }, ...
            ]
            "vttContent": "WEBVTT\n\n1\n00:00:00.031 --> 00:00:03.831\nCome on team, ...",
            "concatenated_text": "Come on team, ...",
            "languages": [ "eng" ],
            "speech_detected": true
            }
          }, ...
        }
        ```

        **AI Content Moderation (CM)**

        The AI Content Moderation API offers a powerful solution for analyzing video
        content to detect various categories of inappropriate material. Leveraging
        state-of-the-art AI models, this API ensures real-time analysis and flagging of
        sensitive or restricted content types, making it an essential tool for platforms
        requiring stringent content moderation.

        Categories:

        - `nsfw`: Quick algorithm to detect pornographic material, ensuring content is
          "not-safe-for-work" or normal.
        - `hard_nudity`: Detailed analysis of video which detects explicit nudity
          involving genitalia.
        - `soft_nudity`: Detailed video analysis that reveals both explicit and partial
          nudity, including the presence of male and female faces and other uncovered
          body parts.
        - `sport`: Recognizes various sporting activities.

        The AI Content Moderation API is an invaluable tool for managing and controlling
        the type of content being shared or streamed on your platform. By implementing
        this API, you can ensure compliance with community guidelines and legal
        requirements, as well as provide a safer environment for your users.

        Important notes:

        - It's allowed to analyze still images too (where applicable). Format of image:
          JPEG, PNG. In that case one image is the same as video of 1 second duration.
        - Not all frames in the video are used for analysis, but only key frames
          (Iframe). For example, if a key frame in a video is set every ±2 seconds, then
          detection will only occur at these timestamps. If an object appears and
          disappears between these time stamps, it will not be detected. We are working
          on a version to analyze more frames, please contact your manager or our
          support team to enable this method.

        Example response with positive result:

        ```
        {
          "status": "SUCCESS",
          "result": {
              "nsfw_detected": true,
              "detection_results": [ "nsfw" ],
              "frames": [
                  {
                      "label": "nsfw",
                      "confidence": 1.0,
                      "frame_number": 24
                  },...
              ]
          }
        }
        ```

        **Additional information**

        Billing takes into account the duration of the analyzed video. Or the duration
        until the stop tag(where applicable), if the condition was triggered during the
        analysis.

        The heart of content moderation is AI, with additional services. They run on our
        own infrastructure, so the files/data are not transferred anywhere to external
        services. After processing, original files are also deleted from local storage
        of AI.

        Read more detailed information about our solution, and architecture, and
        benefits in the knowledge base and blog.

        **Algorithm-specific details**

        Create AI ASR task

        Transcribing is the process of writing down the words you hear in an audio. Our
        solution allows you to transcribe audio from your video and get subtitles
        automatically. To do this, we use modern AI models.

        The result:

        - Transcription – subtitles in the original language. I.e. audio is in English –
          subtitles are in English too, audio is in German – subtitles are in German
          too.
        - Translation – subtitles is translated from the original language to any other
          language.

        **How to use?**

        - Explicit call to this AI method. Applicable for any file stored with us or
          located on the Internet.
        - Standard video upload but with automatic subtitle generation. Look at
          ["VOD uploading"](/api-reference/streaming/videos/create-video).

        **What language will the subtitles be in?**

        You can specify the language explicitly, then it will be used to create
        subtitles: the source language in the audio, the resulting subtitle language. If
        this is not set, the system will run auto language identification and the
        subtitles will be in the detected language. The method also works based on AI
        analysis.

        Additionally, when this is not set, we also support recognition of alternate
        languages in the video (code-switching). For example, when in a video different
        speakers speak several languages, or when they switch from their native language
        to English and back. Thus when you have multiple languages in the video it is
        better to not specify an "audio_language" otherwise AI may force the system to
        recognize gibberish.

        **What can be transcribed?**

        Service uses additional methods to detect presence of speech in audio track,
        thus improving the detection of any human conversations:

        - Speech of one speaker,
        - Speech of several speakers,
        - Speech in different languages,
        - etc

        Restriction on music, lyrics most likely will not be created.

        **What about translation?**

        It is also possible to automatically translate from the original language to
        another you need.

        To create a translation, specify the desired language explicitly in
        "subtitles_language" parameter. Otherwise, the subtitles will be in the original
        language. Translation into different languages should be done by creating
        separate tasks.

        ![Auto generated subtitles example](https://demo-files.gvideo.io/apidocs/captions.gif)

        Use MP4 videos to process. This method is not tied to videos that are stored
        only in our video hosting (look at how get a link to MP4 rendition), so you can
        use links to any other external file with HTTP/HTTPS access.

        For now, only the first audio track can be processed; later this functionality
        will be improved to allow to use any. Also, not all language pairs are currently
        supported. If a language pair is not supported for automatic translation, the
        task status will be FAILURE with description of the reason. Example:
        `eng => uzb`. You can request to add the language pair you need for automatic
        translation. Contact our support.

        Example of modes to transcribe and/or translate:

        - Auto language detection: `{ "url":"..." }`
        - From German language explicitly : `{ "url":"...", "audio_language":"ger" }`
        - From any auto-detected to English language explicitly:
          `{ "url":"...", "subtitles_language":"eng" }`
        - From German language to English language explicitly:
          `{ "url":"...", "audio_language":"ger", "subtitles_language":"eng" }`

        Example of setting a task to process MP4 file (animated gif from above):

        ```
        curl -L 'https://api.gcore.com/streaming/ai/tasks' \\
        -H 'Content-Type: application/json' \\
        -H 'Authorization: APIKey 1234$abcd...' \\
        -d '{
            "url": "https://demo-files.gvideo.io/apidocs/spritefright-blender-cut30sec.mp4"
        }'
        ```

        As described above, transcription is done automatically using AI. Therefore, the
        quality may differ from a manual transcription by a professional person. If this
        happens to you, then you can download subtitles and change them in an external
        editor.

        Transcription and translation are 2 different AI tasks:

        - Transcription is set only for transcription.
        - Translation, if non-original languages are set for translation.

        Billing takes into account the duration of the analyzed original video.

        The heart for transcribing is the AI model Whisper from OpenAI, with additional
        optimizations and services. The AI models run on our own infrastructure, so the
        files/data are not transferred anywhere to external services. After processing,
        original files are also deleted from local storage of AI.

        Read more detailed information about our solution, and architecture, and
        benefits in the knowledge base and blog.

        Create AI CM:nsfw task

        This algorithm allows to quickly detect inappropriate content, determining that
        the content is NSFW ("Not Safe For Work") or normal. Generic info about all
        capabilities and limits see in the generic
        ["Content Moderation"](/api-reference/streaming/ai/create-ai-task) method.

        **What is "Not Safe For Work"?**

        The algorithm has recognized inappropriate content in a video and it might not
        be suitable to view in public places. The solution provides its confidence level
        (in percentage) of how sure it is that the content is NSFW, or it most likely
        does not contain any sexual or similar content.

        Different to soft-nudity-detection and hard-nudity-detection, this model will
        only check for sensitive material that can be considered not-safe-for-work.

        ![AI Content Moderation: NSFW detection visual example](https://demo-files.gvideo.io/apidocs/nsfw-detection.gif)

        **How to use?**

        Frames within the specified video are analyzed.

        Response will contain only frames for which the class nsfw is detected with a
        confidence of more than 50%.

        Example of detected NSFW:

        ```
        {
          "nsfw_detected": true,
          "detection_results": [ "nsfw" ],
          "frames": [
              {
                  "label": "nsfw",
                  "confidence": 0.93,
                  "frame_number": 1
              },..
          ]
        }
        ```

        Example of a response without detecting inappropriate content:

        ```
        {
          "nsfw_detected": false,
          "detection_results": [],
          "frames": []
        }
        ```

        Please note that the API only provides a set of data (json) about the objects
        found, so no video is generated. The demo video video (above ^) was specially
        created based on json from the API for visual demonstration and better
        perception of the possibilities.

        Create AI CM:`hard_nudity` task

        This algorithm allows to detect explicit nudity of the human body (involving
        genitals) in a video. Generic info about all capabilities and limits see in the
        generic ["Content Moderation"](/api-reference/streaming/ai/create-ai-task)
        method.

        **What is Hard nudity detection?**

        This method is often used to analyze UGC to determine whether videos can be
        published to all users, or to prohibit publication due to offensive and
        inappropriate content.

        Objects that can be detected:

        - `ANUS_EXPOSED`
        - `BUTTOCKS_EXPOSED`
        - `FEMALE_BREAST_EXPOSED`
        - `FEMALE_GENITALIA_EXPOSED`
        - `MALE_BREAST_EXPOSED`
        - `MALE_GENITALIA_EXPOSED`

        Please note that the number of objects is less than in the
        soft-nudity-detection. This method works faster and better if only exposed body
        parts detection is required.

        ![AI Content Moderation: hard nudity detection visual example](https://demo-files.gvideo.io/apidocs/nudity_detection.gif)

        **How to use?**

        The information is returned with the video frame number where it was found and
        probability of the detected object. Nudity detection is done using AI, so for
        each object a probability percentage is applied; objects with a probability of
        at least 30% are included in the response.

        Video processing speed is approximately 1:5.

        Example of detected nudity or body parts:

        ```
        {
          "nudity_detected": true,
          "detection_results": [ "MALE_GENITALIA_EXPOSED" ]
          "frames": [
              {
                  "confidence": 0.75,
                  "frame_number": 35,
                  "label": "MALE_GENITALIA_EXPOSED"
              },...
          ]
        }
        ```

        Example response when nudity or body parts were not found:

        ```
        {
          "nudity_detected": false,
          "detection_results": []
          "frames": []
        }
        ```

        There is no universal recipe under which a video can be considered unacceptable,
        since different services host different types of videos for different audiences:
        adult content, children's content, educational content, etc. You can determine
        the probability threshold at which you consider a video inappropriate. The
        easiest option is to run several of your videos and analyze the resulting
        probability coefficient.

        Sometimes a detected object at the beginning of the video immediately makes it
        clear that there is no need to further analyze the video. For such cases, you
        can use stop tags. Use parameter "stop_objects" to specify comma separated stop
        tags. It is also possible to specify % probability threshold value, above which
        the stop tag will be triggered.

        ```
          {
              "url": "...",
              "stop_objects": "MALE_GENITALIA_EXPOSED:0.8,FEMALE_GENITALIA_EXPOSED"
          }
        ```

        Please note that the API only provides a set of data (json) about the objects
        found, so no video is generated. The demo video video (above ^) was specially
        created based on json from the API for visual demonstration and better
        perception of the possibilities.

        Create AI CM:`soft_nudity` task

        This algorithm allows to identify explicit nudity and partial nudity too
        (including the presence of male and female faces and other uncovered body parts)
        in a video. Generic info about all capabilities and limits see in the generic
        ["Content Moderation"](/api-reference/streaming/ai/create-ai-task) method.

        **What is Soft nudity detection?**

        This method is often used to analyze UGC to determine whether videos can be
        published to all users, or to prohibit publication due to offensive and
        inappropriate content.

        Objects that can be detected:

        - `ANUS_COVERED`
        - `ANUS_EXPOSED`
        - `ARMPITS_COVERED`
        - `ARMPITS_EXPOSED`
        - `BELLY_COVERED`
        - `BELLY_EXPOSED`
        - `BUTTOCKS_COVERED`
        - `BUTTOCKS_EXPOSED`
        - `FACE_FEMALE`
        - `FACE_MALE`
        - `FEET_COVERED`
        - `FEET_EXPOSED`
        - `FEMALE_BREAST_COVERED`
        - `FEMALE_BREAST_EXPOSED`
        - `FEMALE_GENITALIA_COVERED`
        - `FEMALE_GENITALIA_EXPOSED`
        - `MALE_BREAST_EXPOSED`
        - `MALE_GENITALIA_EXPOSED`

        This method allows you to identify faces and other body parts. Used to find
        complex combinations of what is happening in a video. Please note that the
        number of objects is more than in the hard-nudity-detection. The method is
        slower.

        ![AI Content Moderation: hard nudity detection visual example](https://demo-files.gvideo.io/apidocs/soft_nudity_detection.gif)

        **How to use?**

        The information is returned with the video frame number where it was found and
        probability of the detected object. Nudity detection is done using AI, so for
        each object a probability percentage is applied; objects with a probability of
        at least 30% are included in the response.

        Video processing speed is approximately 1:5.

        Example of detected nudity or body parts:

        ```
        {
          "nudity_detected": true,
          "detection_results": [ "FACE_FEMALE", "BELLY_COVERED" ]
          "frames": [
              {
                  "confidence": 0.82,
                  "frame_number": 1,
                  "label": "BELLY_COVERED"
              },...
          ]
        }
        ```

        Example response when nudity or body parts were not found:

        ```
        {
          "nudity_detected": false,
          "detection_results": []
          "frames": []
        }
        ```

        There is no universal recipe under which a video can be considered unacceptable,
        since different services host different types of videos for different audiences:
        adult content, children's content, educational content, etc. You can determine
        the probability threshold at which you consider a video inappropriate. The
        easiest option is to run several of your videos and analyze the resulting
        probability coefficient.

        Sometimes a detected object at the beginning of the video immediately makes it
        clear that there is no need to further analyze the video. For such cases, you
        can use stop tags. Use parameter "stop_objects" to specify comma separated stop
        tags. It is also possible to specify % probability threshold value, above which
        the stop tag will be triggered.

        ```
          {
              "url": "...",
              "stop_objects": "BELLY_COVERED:0.9,FEMALE_GENITALIA_COVERED"
          }
        ```

        Please note that the API only provides a set of data (json) about the objects
        found, so no video is generated. The demo video video (above ^) was specially
        created based on json from the API for visual demonstration and better
        perception of the possibilities.

        Create AI CM:sport task

        This algorithm allows to identify various sporting activities in a video.
        Generic info about all capabilities and limits see in the generic
        ["Content Moderation"](/api-reference/streaming/ai/create-ai-task) method.

        **What is Sports activity detection?**

        Sports activity detection by AI involves using machine learning and computer
        vision technologies to automatically identify, analyze, and interpret various
        activities within sports and generic videos. This can include detecting specific
        types, actions, events, and moments.

        This model operates on a video sequence (and not on images as most of the used
        computer vision models). Make sure your video is at least 10-15 seconds long.

        Sports activities can be detected:

        - archery
        - arm wrestling
        - playing badminton
        - playing baseball
        - basketball dunk
        - bowling
        - boxing punch
        - boxing speed bag
        - catching or throwing baseball
        - catching or throwing softball
        - cricket
        - curling
        - disc golfing
        - dodgeball
        - fencing
        - football
        - golf chipping
        - golf driving
        - golf putting
        - hitting baseball
        - hockey stop
        - ice skating
        - javelin throw
        - juggling soccer ball
        - kayaking
        - kicking field goal
        - kicking soccer ball
        - playing cricket
        - playing field hockey
        - playing ice hockey
        - playing kickball
        - playing lacrosse
        - playing ping pong
        - playing polo
        - playing squash or racquetball
        - playing tennis
        - playing volleyball
        - pole vault
        - riding a bike
        - riding or walking with horse
        - roller skating
        - rowing
        - sailing
        - shooting goal (soccer)
        - skateboarding
        - skiing

        Use cases:

        - Sports leagues and content creators can use AI to monitor UGC for unauthorized
          publications of their content. This can include detecting specific sporting
          events or activities that are part of copyrighted content.
        - Sports fans often miss live games and rely on highlight reels. AI can
          automatically detect key moments like goals, touchdowns, or game-winning shots
          in uploaded UGC videos and compile them into personalized highlight reels.

        ![AI Content Moderation: sports activity detection visual example](https://demo-files.gvideo.io/apidocs/sports_football_detection.gif)

        **How to use?**

        The information is returned with the video frame number where it was found and
        probability of the detected activity. Identification is done using AI, so for
        each activity a probability percentage is applied; activities with a probability
        of at least 30% are included in the response.

        Video processing speed is approximately 1:5.

        Example of detected sports activity:

        ```
        {
          "sport_detected": true,
          "detection_results": [ "shooting goal (soccer)" ],
          "frames": [
              {
                  "label": "shooting goal (soccer)",
                  "frame_number": 98,
                  "confidence": 0.99
              },...
          ]
        }
        ```

        Example response when sports activities were not found:

        ```
        {
          "sport_detected": false,
          "detection_results": []
          "frames": []
        }
        ```

        Please note that the API only provides a set of data (json) about the objects
        found, so no video is generated. The demo video video (above ^) was specially
        created based on json from the API for visual demonstration and better
        perception of the possibilities.

        Args:
          category: AI content moderation with "hard_nudity" algorithm

          task_name: Name of the task to be performed

          url: URL to the MP4 file to analyze. File must be publicly accessible via HTTP/HTTPS.

          client_entity_data: Meta parameter, designed to store your own extra information about a video
              entity: video source, video id, etc. It is not used in any way in video
              processing.

              For example, if an AI-task was created automatically when you uploaded a video
              with the AI auto-processing option (nudity detection, etc), then the ID of the
              associated video for which the task was performed will be explicitly indicated
              here.

          client_user_id: Meta parameter, designed to store your own identifier. Can be used by you to tag
              requests from different end-users. It is not used in any way in video
              processing.

          stop_objects: Comma separated objects, and probabilities, that will cause the processing to
              stop immediately after finding.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        category: Literal["soft_nudity"],
        task_name: Literal["content-moderation"],
        url: str,
        client_entity_data: str | Omit = omit,
        client_user_id: str | Omit = omit,
        stop_objects: Literal[
            "ANUS_COVERED",
            "ANUS_EXPOSED",
            "ARMPITS_COVERED",
            "ARMPITS_EXPOSED",
            "BELLY_COVERED",
            "BELLY_EXPOSED",
            "BUTTOCKS_COVERED",
            "BUTTOCKS_EXPOSED",
            "FACE_FEMALE",
            "FACE_MALE",
            "FEET_COVERED",
            "FEET_EXPOSED",
            "FEMALE_BREAST_COVERED",
            "FEMALE_BREAST_EXPOSED",
            "FEMALE_GENITALIA_COVERED",
            "FEMALE_GENITALIA_EXPOSED",
            "MALE_BREAST_EXPOSED",
            "MALE_GENITALIA_EXPOSED",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AITaskCreateResponse:
        """
        Creating an AI task.

        This method allows you to create an AI task for VOD video processing:

        - ASR: Transcribe video
        - ASR: Translate subtitles
        - CM: Sports detection
        - CM: Not Safe For Work (NSFW) content detection
        - CM: Soft nudity detection
        - CM: Hard nudity detection
        - CM: Objects recognition (soon)

        ![Auto generated subtitles example](https://demo-files.gvideo.io/apidocs/captions.gif)

        How to use:

        - Create an AI task, specify algorithm to use
        - Get `task_id`
        - Check a result using `.../ai/tasks/{task_id}` method

        For more detailed information, see the algorithm-specific sections below.

        **AI Automatic Speech Recognition (ASR)**

        AI is instrumental in automatic video processing for subtitles creation by using
        Automatic Speech Recognition (ASR) technology to transcribe spoken words into
        text, which can then be translated into multiple languages for broader
        accessibility.

        Categories:

        - `transcription` – to create subtitles/captions from audio in the original
          language.
        - `translation` – to translate subtitles/captions from the original language to
          99+ other languages.

        AI subtitle transcription and translation tools are highly efficient, processing
        large volumes of audio-visual content quickly and providing accurate
        transcriptions and translations with minimal human intervention. Additionally,
        AI-driven solutions can significantly reduce costs and turnaround times compared
        to traditional methods, making them an invaluable resource for content creators
        and broadcasters aiming to reach global audiences.

        Example response with positive result:

        ```
        {
          "status": "SUCCESS",
          "result": {
            "subtitles": [
              {
                  "start_time": "00:00:00.031",
                  "end_time": "00:00:03.831",
                  "text": "Come on team, ..."
              }, ...
            ]
            "vttContent": "WEBVTT\n\n1\n00:00:00.031 --> 00:00:03.831\nCome on team, ...",
            "concatenated_text": "Come on team, ...",
            "languages": [ "eng" ],
            "speech_detected": true
            }
          }, ...
        }
        ```

        **AI Content Moderation (CM)**

        The AI Content Moderation API offers a powerful solution for analyzing video
        content to detect various categories of inappropriate material. Leveraging
        state-of-the-art AI models, this API ensures real-time analysis and flagging of
        sensitive or restricted content types, making it an essential tool for platforms
        requiring stringent content moderation.

        Categories:

        - `nsfw`: Quick algorithm to detect pornographic material, ensuring content is
          "not-safe-for-work" or normal.
        - `hard_nudity`: Detailed analysis of video which detects explicit nudity
          involving genitalia.
        - `soft_nudity`: Detailed video analysis that reveals both explicit and partial
          nudity, including the presence of male and female faces and other uncovered
          body parts.
        - `sport`: Recognizes various sporting activities.

        The AI Content Moderation API is an invaluable tool for managing and controlling
        the type of content being shared or streamed on your platform. By implementing
        this API, you can ensure compliance with community guidelines and legal
        requirements, as well as provide a safer environment for your users.

        Important notes:

        - It's allowed to analyze still images too (where applicable). Format of image:
          JPEG, PNG. In that case one image is the same as video of 1 second duration.
        - Not all frames in the video are used for analysis, but only key frames
          (Iframe). For example, if a key frame in a video is set every ±2 seconds, then
          detection will only occur at these timestamps. If an object appears and
          disappears between these time stamps, it will not be detected. We are working
          on a version to analyze more frames, please contact your manager or our
          support team to enable this method.

        Example response with positive result:

        ```
        {
          "status": "SUCCESS",
          "result": {
              "nsfw_detected": true,
              "detection_results": [ "nsfw" ],
              "frames": [
                  {
                      "label": "nsfw",
                      "confidence": 1.0,
                      "frame_number": 24
                  },...
              ]
          }
        }
        ```

        **Additional information**

        Billing takes into account the duration of the analyzed video. Or the duration
        until the stop tag(where applicable), if the condition was triggered during the
        analysis.

        The heart of content moderation is AI, with additional services. They run on our
        own infrastructure, so the files/data are not transferred anywhere to external
        services. After processing, original files are also deleted from local storage
        of AI.

        Read more detailed information about our solution, and architecture, and
        benefits in the knowledge base and blog.

        **Algorithm-specific details**

        Create AI ASR task

        Transcribing is the process of writing down the words you hear in an audio. Our
        solution allows you to transcribe audio from your video and get subtitles
        automatically. To do this, we use modern AI models.

        The result:

        - Transcription – subtitles in the original language. I.e. audio is in English –
          subtitles are in English too, audio is in German – subtitles are in German
          too.
        - Translation – subtitles is translated from the original language to any other
          language.

        **How to use?**

        - Explicit call to this AI method. Applicable for any file stored with us or
          located on the Internet.
        - Standard video upload but with automatic subtitle generation. Look at
          ["VOD uploading"](/api-reference/streaming/videos/create-video).

        **What language will the subtitles be in?**

        You can specify the language explicitly, then it will be used to create
        subtitles: the source language in the audio, the resulting subtitle language. If
        this is not set, the system will run auto language identification and the
        subtitles will be in the detected language. The method also works based on AI
        analysis.

        Additionally, when this is not set, we also support recognition of alternate
        languages in the video (code-switching). For example, when in a video different
        speakers speak several languages, or when they switch from their native language
        to English and back. Thus when you have multiple languages in the video it is
        better to not specify an "audio_language" otherwise AI may force the system to
        recognize gibberish.

        **What can be transcribed?**

        Service uses additional methods to detect presence of speech in audio track,
        thus improving the detection of any human conversations:

        - Speech of one speaker,
        - Speech of several speakers,
        - Speech in different languages,
        - etc

        Restriction on music, lyrics most likely will not be created.

        **What about translation?**

        It is also possible to automatically translate from the original language to
        another you need.

        To create a translation, specify the desired language explicitly in
        "subtitles_language" parameter. Otherwise, the subtitles will be in the original
        language. Translation into different languages should be done by creating
        separate tasks.

        ![Auto generated subtitles example](https://demo-files.gvideo.io/apidocs/captions.gif)

        Use MP4 videos to process. This method is not tied to videos that are stored
        only in our video hosting (look at how get a link to MP4 rendition), so you can
        use links to any other external file with HTTP/HTTPS access.

        For now, only the first audio track can be processed; later this functionality
        will be improved to allow to use any. Also, not all language pairs are currently
        supported. If a language pair is not supported for automatic translation, the
        task status will be FAILURE with description of the reason. Example:
        `eng => uzb`. You can request to add the language pair you need for automatic
        translation. Contact our support.

        Example of modes to transcribe and/or translate:

        - Auto language detection: `{ "url":"..." }`
        - From German language explicitly : `{ "url":"...", "audio_language":"ger" }`
        - From any auto-detected to English language explicitly:
          `{ "url":"...", "subtitles_language":"eng" }`
        - From German language to English language explicitly:
          `{ "url":"...", "audio_language":"ger", "subtitles_language":"eng" }`

        Example of setting a task to process MP4 file (animated gif from above):

        ```
        curl -L 'https://api.gcore.com/streaming/ai/tasks' \\
        -H 'Content-Type: application/json' \\
        -H 'Authorization: APIKey 1234$abcd...' \\
        -d '{
            "url": "https://demo-files.gvideo.io/apidocs/spritefright-blender-cut30sec.mp4"
        }'
        ```

        As described above, transcription is done automatically using AI. Therefore, the
        quality may differ from a manual transcription by a professional person. If this
        happens to you, then you can download subtitles and change them in an external
        editor.

        Transcription and translation are 2 different AI tasks:

        - Transcription is set only for transcription.
        - Translation, if non-original languages are set for translation.

        Billing takes into account the duration of the analyzed original video.

        The heart for transcribing is the AI model Whisper from OpenAI, with additional
        optimizations and services. The AI models run on our own infrastructure, so the
        files/data are not transferred anywhere to external services. After processing,
        original files are also deleted from local storage of AI.

        Read more detailed information about our solution, and architecture, and
        benefits in the knowledge base and blog.

        Create AI CM:nsfw task

        This algorithm allows to quickly detect inappropriate content, determining that
        the content is NSFW ("Not Safe For Work") or normal. Generic info about all
        capabilities and limits see in the generic
        ["Content Moderation"](/api-reference/streaming/ai/create-ai-task) method.

        **What is "Not Safe For Work"?**

        The algorithm has recognized inappropriate content in a video and it might not
        be suitable to view in public places. The solution provides its confidence level
        (in percentage) of how sure it is that the content is NSFW, or it most likely
        does not contain any sexual or similar content.

        Different to soft-nudity-detection and hard-nudity-detection, this model will
        only check for sensitive material that can be considered not-safe-for-work.

        ![AI Content Moderation: NSFW detection visual example](https://demo-files.gvideo.io/apidocs/nsfw-detection.gif)

        **How to use?**

        Frames within the specified video are analyzed.

        Response will contain only frames for which the class nsfw is detected with a
        confidence of more than 50%.

        Example of detected NSFW:

        ```
        {
          "nsfw_detected": true,
          "detection_results": [ "nsfw" ],
          "frames": [
              {
                  "label": "nsfw",
                  "confidence": 0.93,
                  "frame_number": 1
              },..
          ]
        }
        ```

        Example of a response without detecting inappropriate content:

        ```
        {
          "nsfw_detected": false,
          "detection_results": [],
          "frames": []
        }
        ```

        Please note that the API only provides a set of data (json) about the objects
        found, so no video is generated. The demo video video (above ^) was specially
        created based on json from the API for visual demonstration and better
        perception of the possibilities.

        Create AI CM:`hard_nudity` task

        This algorithm allows to detect explicit nudity of the human body (involving
        genitals) in a video. Generic info about all capabilities and limits see in the
        generic ["Content Moderation"](/api-reference/streaming/ai/create-ai-task)
        method.

        **What is Hard nudity detection?**

        This method is often used to analyze UGC to determine whether videos can be
        published to all users, or to prohibit publication due to offensive and
        inappropriate content.

        Objects that can be detected:

        - `ANUS_EXPOSED`
        - `BUTTOCKS_EXPOSED`
        - `FEMALE_BREAST_EXPOSED`
        - `FEMALE_GENITALIA_EXPOSED`
        - `MALE_BREAST_EXPOSED`
        - `MALE_GENITALIA_EXPOSED`

        Please note that the number of objects is less than in the
        soft-nudity-detection. This method works faster and better if only exposed body
        parts detection is required.

        ![AI Content Moderation: hard nudity detection visual example](https://demo-files.gvideo.io/apidocs/nudity_detection.gif)

        **How to use?**

        The information is returned with the video frame number where it was found and
        probability of the detected object. Nudity detection is done using AI, so for
        each object a probability percentage is applied; objects with a probability of
        at least 30% are included in the response.

        Video processing speed is approximately 1:5.

        Example of detected nudity or body parts:

        ```
        {
          "nudity_detected": true,
          "detection_results": [ "MALE_GENITALIA_EXPOSED" ]
          "frames": [
              {
                  "confidence": 0.75,
                  "frame_number": 35,
                  "label": "MALE_GENITALIA_EXPOSED"
              },...
          ]
        }
        ```

        Example response when nudity or body parts were not found:

        ```
        {
          "nudity_detected": false,
          "detection_results": []
          "frames": []
        }
        ```

        There is no universal recipe under which a video can be considered unacceptable,
        since different services host different types of videos for different audiences:
        adult content, children's content, educational content, etc. You can determine
        the probability threshold at which you consider a video inappropriate. The
        easiest option is to run several of your videos and analyze the resulting
        probability coefficient.

        Sometimes a detected object at the beginning of the video immediately makes it
        clear that there is no need to further analyze the video. For such cases, you
        can use stop tags. Use parameter "stop_objects" to specify comma separated stop
        tags. It is also possible to specify % probability threshold value, above which
        the stop tag will be triggered.

        ```
          {
              "url": "...",
              "stop_objects": "MALE_GENITALIA_EXPOSED:0.8,FEMALE_GENITALIA_EXPOSED"
          }
        ```

        Please note that the API only provides a set of data (json) about the objects
        found, so no video is generated. The demo video video (above ^) was specially
        created based on json from the API for visual demonstration and better
        perception of the possibilities.

        Create AI CM:`soft_nudity` task

        This algorithm allows to identify explicit nudity and partial nudity too
        (including the presence of male and female faces and other uncovered body parts)
        in a video. Generic info about all capabilities and limits see in the generic
        ["Content Moderation"](/api-reference/streaming/ai/create-ai-task) method.

        **What is Soft nudity detection?**

        This method is often used to analyze UGC to determine whether videos can be
        published to all users, or to prohibit publication due to offensive and
        inappropriate content.

        Objects that can be detected:

        - `ANUS_COVERED`
        - `ANUS_EXPOSED`
        - `ARMPITS_COVERED`
        - `ARMPITS_EXPOSED`
        - `BELLY_COVERED`
        - `BELLY_EXPOSED`
        - `BUTTOCKS_COVERED`
        - `BUTTOCKS_EXPOSED`
        - `FACE_FEMALE`
        - `FACE_MALE`
        - `FEET_COVERED`
        - `FEET_EXPOSED`
        - `FEMALE_BREAST_COVERED`
        - `FEMALE_BREAST_EXPOSED`
        - `FEMALE_GENITALIA_COVERED`
        - `FEMALE_GENITALIA_EXPOSED`
        - `MALE_BREAST_EXPOSED`
        - `MALE_GENITALIA_EXPOSED`

        This method allows you to identify faces and other body parts. Used to find
        complex combinations of what is happening in a video. Please note that the
        number of objects is more than in the hard-nudity-detection. The method is
        slower.

        ![AI Content Moderation: hard nudity detection visual example](https://demo-files.gvideo.io/apidocs/soft_nudity_detection.gif)

        **How to use?**

        The information is returned with the video frame number where it was found and
        probability of the detected object. Nudity detection is done using AI, so for
        each object a probability percentage is applied; objects with a probability of
        at least 30% are included in the response.

        Video processing speed is approximately 1:5.

        Example of detected nudity or body parts:

        ```
        {
          "nudity_detected": true,
          "detection_results": [ "FACE_FEMALE", "BELLY_COVERED" ]
          "frames": [
              {
                  "confidence": 0.82,
                  "frame_number": 1,
                  "label": "BELLY_COVERED"
              },...
          ]
        }
        ```

        Example response when nudity or body parts were not found:

        ```
        {
          "nudity_detected": false,
          "detection_results": []
          "frames": []
        }
        ```

        There is no universal recipe under which a video can be considered unacceptable,
        since different services host different types of videos for different audiences:
        adult content, children's content, educational content, etc. You can determine
        the probability threshold at which you consider a video inappropriate. The
        easiest option is to run several of your videos and analyze the resulting
        probability coefficient.

        Sometimes a detected object at the beginning of the video immediately makes it
        clear that there is no need to further analyze the video. For such cases, you
        can use stop tags. Use parameter "stop_objects" to specify comma separated stop
        tags. It is also possible to specify % probability threshold value, above which
        the stop tag will be triggered.

        ```
          {
              "url": "...",
              "stop_objects": "BELLY_COVERED:0.9,FEMALE_GENITALIA_COVERED"
          }
        ```

        Please note that the API only provides a set of data (json) about the objects
        found, so no video is generated. The demo video video (above ^) was specially
        created based on json from the API for visual demonstration and better
        perception of the possibilities.

        Create AI CM:sport task

        This algorithm allows to identify various sporting activities in a video.
        Generic info about all capabilities and limits see in the generic
        ["Content Moderation"](/api-reference/streaming/ai/create-ai-task) method.

        **What is Sports activity detection?**

        Sports activity detection by AI involves using machine learning and computer
        vision technologies to automatically identify, analyze, and interpret various
        activities within sports and generic videos. This can include detecting specific
        types, actions, events, and moments.

        This model operates on a video sequence (and not on images as most of the used
        computer vision models). Make sure your video is at least 10-15 seconds long.

        Sports activities can be detected:

        - archery
        - arm wrestling
        - playing badminton
        - playing baseball
        - basketball dunk
        - bowling
        - boxing punch
        - boxing speed bag
        - catching or throwing baseball
        - catching or throwing softball
        - cricket
        - curling
        - disc golfing
        - dodgeball
        - fencing
        - football
        - golf chipping
        - golf driving
        - golf putting
        - hitting baseball
        - hockey stop
        - ice skating
        - javelin throw
        - juggling soccer ball
        - kayaking
        - kicking field goal
        - kicking soccer ball
        - playing cricket
        - playing field hockey
        - playing ice hockey
        - playing kickball
        - playing lacrosse
        - playing ping pong
        - playing polo
        - playing squash or racquetball
        - playing tennis
        - playing volleyball
        - pole vault
        - riding a bike
        - riding or walking with horse
        - roller skating
        - rowing
        - sailing
        - shooting goal (soccer)
        - skateboarding
        - skiing

        Use cases:

        - Sports leagues and content creators can use AI to monitor UGC for unauthorized
          publications of their content. This can include detecting specific sporting
          events or activities that are part of copyrighted content.
        - Sports fans often miss live games and rely on highlight reels. AI can
          automatically detect key moments like goals, touchdowns, or game-winning shots
          in uploaded UGC videos and compile them into personalized highlight reels.

        ![AI Content Moderation: sports activity detection visual example](https://demo-files.gvideo.io/apidocs/sports_football_detection.gif)

        **How to use?**

        The information is returned with the video frame number where it was found and
        probability of the detected activity. Identification is done using AI, so for
        each activity a probability percentage is applied; activities with a probability
        of at least 30% are included in the response.

        Video processing speed is approximately 1:5.

        Example of detected sports activity:

        ```
        {
          "sport_detected": true,
          "detection_results": [ "shooting goal (soccer)" ],
          "frames": [
              {
                  "label": "shooting goal (soccer)",
                  "frame_number": 98,
                  "confidence": 0.99
              },...
          ]
        }
        ```

        Example response when sports activities were not found:

        ```
        {
          "sport_detected": false,
          "detection_results": []
          "frames": []
        }
        ```

        Please note that the API only provides a set of data (json) about the objects
        found, so no video is generated. The demo video video (above ^) was specially
        created based on json from the API for visual demonstration and better
        perception of the possibilities.

        Args:
          category: AI content moderation with "soft_nudity" algorithm

          task_name: Name of the task to be performed

          url: URL to the MP4 file to analyze. File must be publicly accessible via HTTP/HTTPS.

          client_entity_data: Meta parameter, designed to store your own extra information about a video
              entity: video source, video id, etc. It is not used in any way in video
              processing.

              For example, if an AI-task was created automatically when you uploaded a video
              with the AI auto-processing option (nudity detection, etc), then the ID of the
              associated video for which the task was performed will be explicitly indicated
              here.

          client_user_id: Meta parameter, designed to store your own identifier. Can be used by you to tag
              requests from different end-users. It is not used in any way in video
              processing.

          stop_objects: Comma separated objects, and probabilities, that will cause the processing to
              stop immediately after finding.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        category: Literal["sport"],
        task_name: Literal["content-moderation"],
        url: str,
        client_entity_data: str | Omit = omit,
        client_user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AITaskCreateResponse:
        """
        Creating an AI task.

        This method allows you to create an AI task for VOD video processing:

        - ASR: Transcribe video
        - ASR: Translate subtitles
        - CM: Sports detection
        - CM: Not Safe For Work (NSFW) content detection
        - CM: Soft nudity detection
        - CM: Hard nudity detection
        - CM: Objects recognition (soon)

        ![Auto generated subtitles example](https://demo-files.gvideo.io/apidocs/captions.gif)

        How to use:

        - Create an AI task, specify algorithm to use
        - Get `task_id`
        - Check a result using `.../ai/tasks/{task_id}` method

        For more detailed information, see the algorithm-specific sections below.

        **AI Automatic Speech Recognition (ASR)**

        AI is instrumental in automatic video processing for subtitles creation by using
        Automatic Speech Recognition (ASR) technology to transcribe spoken words into
        text, which can then be translated into multiple languages for broader
        accessibility.

        Categories:

        - `transcription` – to create subtitles/captions from audio in the original
          language.
        - `translation` – to translate subtitles/captions from the original language to
          99+ other languages.

        AI subtitle transcription and translation tools are highly efficient, processing
        large volumes of audio-visual content quickly and providing accurate
        transcriptions and translations with minimal human intervention. Additionally,
        AI-driven solutions can significantly reduce costs and turnaround times compared
        to traditional methods, making them an invaluable resource for content creators
        and broadcasters aiming to reach global audiences.

        Example response with positive result:

        ```
        {
          "status": "SUCCESS",
          "result": {
            "subtitles": [
              {
                  "start_time": "00:00:00.031",
                  "end_time": "00:00:03.831",
                  "text": "Come on team, ..."
              }, ...
            ]
            "vttContent": "WEBVTT\n\n1\n00:00:00.031 --> 00:00:03.831\nCome on team, ...",
            "concatenated_text": "Come on team, ...",
            "languages": [ "eng" ],
            "speech_detected": true
            }
          }, ...
        }
        ```

        **AI Content Moderation (CM)**

        The AI Content Moderation API offers a powerful solution for analyzing video
        content to detect various categories of inappropriate material. Leveraging
        state-of-the-art AI models, this API ensures real-time analysis and flagging of
        sensitive or restricted content types, making it an essential tool for platforms
        requiring stringent content moderation.

        Categories:

        - `nsfw`: Quick algorithm to detect pornographic material, ensuring content is
          "not-safe-for-work" or normal.
        - `hard_nudity`: Detailed analysis of video which detects explicit nudity
          involving genitalia.
        - `soft_nudity`: Detailed video analysis that reveals both explicit and partial
          nudity, including the presence of male and female faces and other uncovered
          body parts.
        - `sport`: Recognizes various sporting activities.

        The AI Content Moderation API is an invaluable tool for managing and controlling
        the type of content being shared or streamed on your platform. By implementing
        this API, you can ensure compliance with community guidelines and legal
        requirements, as well as provide a safer environment for your users.

        Important notes:

        - It's allowed to analyze still images too (where applicable). Format of image:
          JPEG, PNG. In that case one image is the same as video of 1 second duration.
        - Not all frames in the video are used for analysis, but only key frames
          (Iframe). For example, if a key frame in a video is set every ±2 seconds, then
          detection will only occur at these timestamps. If an object appears and
          disappears between these time stamps, it will not be detected. We are working
          on a version to analyze more frames, please contact your manager or our
          support team to enable this method.

        Example response with positive result:

        ```
        {
          "status": "SUCCESS",
          "result": {
              "nsfw_detected": true,
              "detection_results": [ "nsfw" ],
              "frames": [
                  {
                      "label": "nsfw",
                      "confidence": 1.0,
                      "frame_number": 24
                  },...
              ]
          }
        }
        ```

        **Additional information**

        Billing takes into account the duration of the analyzed video. Or the duration
        until the stop tag(where applicable), if the condition was triggered during the
        analysis.

        The heart of content moderation is AI, with additional services. They run on our
        own infrastructure, so the files/data are not transferred anywhere to external
        services. After processing, original files are also deleted from local storage
        of AI.

        Read more detailed information about our solution, and architecture, and
        benefits in the knowledge base and blog.

        **Algorithm-specific details**

        Create AI ASR task

        Transcribing is the process of writing down the words you hear in an audio. Our
        solution allows you to transcribe audio from your video and get subtitles
        automatically. To do this, we use modern AI models.

        The result:

        - Transcription – subtitles in the original language. I.e. audio is in English –
          subtitles are in English too, audio is in German – subtitles are in German
          too.
        - Translation – subtitles is translated from the original language to any other
          language.

        **How to use?**

        - Explicit call to this AI method. Applicable for any file stored with us or
          located on the Internet.
        - Standard video upload but with automatic subtitle generation. Look at
          ["VOD uploading"](/api-reference/streaming/videos/create-video).

        **What language will the subtitles be in?**

        You can specify the language explicitly, then it will be used to create
        subtitles: the source language in the audio, the resulting subtitle language. If
        this is not set, the system will run auto language identification and the
        subtitles will be in the detected language. The method also works based on AI
        analysis.

        Additionally, when this is not set, we also support recognition of alternate
        languages in the video (code-switching). For example, when in a video different
        speakers speak several languages, or when they switch from their native language
        to English and back. Thus when you have multiple languages in the video it is
        better to not specify an "audio_language" otherwise AI may force the system to
        recognize gibberish.

        **What can be transcribed?**

        Service uses additional methods to detect presence of speech in audio track,
        thus improving the detection of any human conversations:

        - Speech of one speaker,
        - Speech of several speakers,
        - Speech in different languages,
        - etc

        Restriction on music, lyrics most likely will not be created.

        **What about translation?**

        It is also possible to automatically translate from the original language to
        another you need.

        To create a translation, specify the desired language explicitly in
        "subtitles_language" parameter. Otherwise, the subtitles will be in the original
        language. Translation into different languages should be done by creating
        separate tasks.

        ![Auto generated subtitles example](https://demo-files.gvideo.io/apidocs/captions.gif)

        Use MP4 videos to process. This method is not tied to videos that are stored
        only in our video hosting (look at how get a link to MP4 rendition), so you can
        use links to any other external file with HTTP/HTTPS access.

        For now, only the first audio track can be processed; later this functionality
        will be improved to allow to use any. Also, not all language pairs are currently
        supported. If a language pair is not supported for automatic translation, the
        task status will be FAILURE with description of the reason. Example:
        `eng => uzb`. You can request to add the language pair you need for automatic
        translation. Contact our support.

        Example of modes to transcribe and/or translate:

        - Auto language detection: `{ "url":"..." }`
        - From German language explicitly : `{ "url":"...", "audio_language":"ger" }`
        - From any auto-detected to English language explicitly:
          `{ "url":"...", "subtitles_language":"eng" }`
        - From German language to English language explicitly:
          `{ "url":"...", "audio_language":"ger", "subtitles_language":"eng" }`

        Example of setting a task to process MP4 file (animated gif from above):

        ```
        curl -L 'https://api.gcore.com/streaming/ai/tasks' \\
        -H 'Content-Type: application/json' \\
        -H 'Authorization: APIKey 1234$abcd...' \\
        -d '{
            "url": "https://demo-files.gvideo.io/apidocs/spritefright-blender-cut30sec.mp4"
        }'
        ```

        As described above, transcription is done automatically using AI. Therefore, the
        quality may differ from a manual transcription by a professional person. If this
        happens to you, then you can download subtitles and change them in an external
        editor.

        Transcription and translation are 2 different AI tasks:

        - Transcription is set only for transcription.
        - Translation, if non-original languages are set for translation.

        Billing takes into account the duration of the analyzed original video.

        The heart for transcribing is the AI model Whisper from OpenAI, with additional
        optimizations and services. The AI models run on our own infrastructure, so the
        files/data are not transferred anywhere to external services. After processing,
        original files are also deleted from local storage of AI.

        Read more detailed information about our solution, and architecture, and
        benefits in the knowledge base and blog.

        Create AI CM:nsfw task

        This algorithm allows to quickly detect inappropriate content, determining that
        the content is NSFW ("Not Safe For Work") or normal. Generic info about all
        capabilities and limits see in the generic
        ["Content Moderation"](/api-reference/streaming/ai/create-ai-task) method.

        **What is "Not Safe For Work"?**

        The algorithm has recognized inappropriate content in a video and it might not
        be suitable to view in public places. The solution provides its confidence level
        (in percentage) of how sure it is that the content is NSFW, or it most likely
        does not contain any sexual or similar content.

        Different to soft-nudity-detection and hard-nudity-detection, this model will
        only check for sensitive material that can be considered not-safe-for-work.

        ![AI Content Moderation: NSFW detection visual example](https://demo-files.gvideo.io/apidocs/nsfw-detection.gif)

        **How to use?**

        Frames within the specified video are analyzed.

        Response will contain only frames for which the class nsfw is detected with a
        confidence of more than 50%.

        Example of detected NSFW:

        ```
        {
          "nsfw_detected": true,
          "detection_results": [ "nsfw" ],
          "frames": [
              {
                  "label": "nsfw",
                  "confidence": 0.93,
                  "frame_number": 1
              },..
          ]
        }
        ```

        Example of a response without detecting inappropriate content:

        ```
        {
          "nsfw_detected": false,
          "detection_results": [],
          "frames": []
        }
        ```

        Please note that the API only provides a set of data (json) about the objects
        found, so no video is generated. The demo video video (above ^) was specially
        created based on json from the API for visual demonstration and better
        perception of the possibilities.

        Create AI CM:`hard_nudity` task

        This algorithm allows to detect explicit nudity of the human body (involving
        genitals) in a video. Generic info about all capabilities and limits see in the
        generic ["Content Moderation"](/api-reference/streaming/ai/create-ai-task)
        method.

        **What is Hard nudity detection?**

        This method is often used to analyze UGC to determine whether videos can be
        published to all users, or to prohibit publication due to offensive and
        inappropriate content.

        Objects that can be detected:

        - `ANUS_EXPOSED`
        - `BUTTOCKS_EXPOSED`
        - `FEMALE_BREAST_EXPOSED`
        - `FEMALE_GENITALIA_EXPOSED`
        - `MALE_BREAST_EXPOSED`
        - `MALE_GENITALIA_EXPOSED`

        Please note that the number of objects is less than in the
        soft-nudity-detection. This method works faster and better if only exposed body
        parts detection is required.

        ![AI Content Moderation: hard nudity detection visual example](https://demo-files.gvideo.io/apidocs/nudity_detection.gif)

        **How to use?**

        The information is returned with the video frame number where it was found and
        probability of the detected object. Nudity detection is done using AI, so for
        each object a probability percentage is applied; objects with a probability of
        at least 30% are included in the response.

        Video processing speed is approximately 1:5.

        Example of detected nudity or body parts:

        ```
        {
          "nudity_detected": true,
          "detection_results": [ "MALE_GENITALIA_EXPOSED" ]
          "frames": [
              {
                  "confidence": 0.75,
                  "frame_number": 35,
                  "label": "MALE_GENITALIA_EXPOSED"
              },...
          ]
        }
        ```

        Example response when nudity or body parts were not found:

        ```
        {
          "nudity_detected": false,
          "detection_results": []
          "frames": []
        }
        ```

        There is no universal recipe under which a video can be considered unacceptable,
        since different services host different types of videos for different audiences:
        adult content, children's content, educational content, etc. You can determine
        the probability threshold at which you consider a video inappropriate. The
        easiest option is to run several of your videos and analyze the resulting
        probability coefficient.

        Sometimes a detected object at the beginning of the video immediately makes it
        clear that there is no need to further analyze the video. For such cases, you
        can use stop tags. Use parameter "stop_objects" to specify comma separated stop
        tags. It is also possible to specify % probability threshold value, above which
        the stop tag will be triggered.

        ```
          {
              "url": "...",
              "stop_objects": "MALE_GENITALIA_EXPOSED:0.8,FEMALE_GENITALIA_EXPOSED"
          }
        ```

        Please note that the API only provides a set of data (json) about the objects
        found, so no video is generated. The demo video video (above ^) was specially
        created based on json from the API for visual demonstration and better
        perception of the possibilities.

        Create AI CM:`soft_nudity` task

        This algorithm allows to identify explicit nudity and partial nudity too
        (including the presence of male and female faces and other uncovered body parts)
        in a video. Generic info about all capabilities and limits see in the generic
        ["Content Moderation"](/api-reference/streaming/ai/create-ai-task) method.

        **What is Soft nudity detection?**

        This method is often used to analyze UGC to determine whether videos can be
        published to all users, or to prohibit publication due to offensive and
        inappropriate content.

        Objects that can be detected:

        - `ANUS_COVERED`
        - `ANUS_EXPOSED`
        - `ARMPITS_COVERED`
        - `ARMPITS_EXPOSED`
        - `BELLY_COVERED`
        - `BELLY_EXPOSED`
        - `BUTTOCKS_COVERED`
        - `BUTTOCKS_EXPOSED`
        - `FACE_FEMALE`
        - `FACE_MALE`
        - `FEET_COVERED`
        - `FEET_EXPOSED`
        - `FEMALE_BREAST_COVERED`
        - `FEMALE_BREAST_EXPOSED`
        - `FEMALE_GENITALIA_COVERED`
        - `FEMALE_GENITALIA_EXPOSED`
        - `MALE_BREAST_EXPOSED`
        - `MALE_GENITALIA_EXPOSED`

        This method allows you to identify faces and other body parts. Used to find
        complex combinations of what is happening in a video. Please note that the
        number of objects is more than in the hard-nudity-detection. The method is
        slower.

        ![AI Content Moderation: hard nudity detection visual example](https://demo-files.gvideo.io/apidocs/soft_nudity_detection.gif)

        **How to use?**

        The information is returned with the video frame number where it was found and
        probability of the detected object. Nudity detection is done using AI, so for
        each object a probability percentage is applied; objects with a probability of
        at least 30% are included in the response.

        Video processing speed is approximately 1:5.

        Example of detected nudity or body parts:

        ```
        {
          "nudity_detected": true,
          "detection_results": [ "FACE_FEMALE", "BELLY_COVERED" ]
          "frames": [
              {
                  "confidence": 0.82,
                  "frame_number": 1,
                  "label": "BELLY_COVERED"
              },...
          ]
        }
        ```

        Example response when nudity or body parts were not found:

        ```
        {
          "nudity_detected": false,
          "detection_results": []
          "frames": []
        }
        ```

        There is no universal recipe under which a video can be considered unacceptable,
        since different services host different types of videos for different audiences:
        adult content, children's content, educational content, etc. You can determine
        the probability threshold at which you consider a video inappropriate. The
        easiest option is to run several of your videos and analyze the resulting
        probability coefficient.

        Sometimes a detected object at the beginning of the video immediately makes it
        clear that there is no need to further analyze the video. For such cases, you
        can use stop tags. Use parameter "stop_objects" to specify comma separated stop
        tags. It is also possible to specify % probability threshold value, above which
        the stop tag will be triggered.

        ```
          {
              "url": "...",
              "stop_objects": "BELLY_COVERED:0.9,FEMALE_GENITALIA_COVERED"
          }
        ```

        Please note that the API only provides a set of data (json) about the objects
        found, so no video is generated. The demo video video (above ^) was specially
        created based on json from the API for visual demonstration and better
        perception of the possibilities.

        Create AI CM:sport task

        This algorithm allows to identify various sporting activities in a video.
        Generic info about all capabilities and limits see in the generic
        ["Content Moderation"](/api-reference/streaming/ai/create-ai-task) method.

        **What is Sports activity detection?**

        Sports activity detection by AI involves using machine learning and computer
        vision technologies to automatically identify, analyze, and interpret various
        activities within sports and generic videos. This can include detecting specific
        types, actions, events, and moments.

        This model operates on a video sequence (and not on images as most of the used
        computer vision models). Make sure your video is at least 10-15 seconds long.

        Sports activities can be detected:

        - archery
        - arm wrestling
        - playing badminton
        - playing baseball
        - basketball dunk
        - bowling
        - boxing punch
        - boxing speed bag
        - catching or throwing baseball
        - catching or throwing softball
        - cricket
        - curling
        - disc golfing
        - dodgeball
        - fencing
        - football
        - golf chipping
        - golf driving
        - golf putting
        - hitting baseball
        - hockey stop
        - ice skating
        - javelin throw
        - juggling soccer ball
        - kayaking
        - kicking field goal
        - kicking soccer ball
        - playing cricket
        - playing field hockey
        - playing ice hockey
        - playing kickball
        - playing lacrosse
        - playing ping pong
        - playing polo
        - playing squash or racquetball
        - playing tennis
        - playing volleyball
        - pole vault
        - riding a bike
        - riding or walking with horse
        - roller skating
        - rowing
        - sailing
        - shooting goal (soccer)
        - skateboarding
        - skiing

        Use cases:

        - Sports leagues and content creators can use AI to monitor UGC for unauthorized
          publications of their content. This can include detecting specific sporting
          events or activities that are part of copyrighted content.
        - Sports fans often miss live games and rely on highlight reels. AI can
          automatically detect key moments like goals, touchdowns, or game-winning shots
          in uploaded UGC videos and compile them into personalized highlight reels.

        ![AI Content Moderation: sports activity detection visual example](https://demo-files.gvideo.io/apidocs/sports_football_detection.gif)

        **How to use?**

        The information is returned with the video frame number where it was found and
        probability of the detected activity. Identification is done using AI, so for
        each activity a probability percentage is applied; activities with a probability
        of at least 30% are included in the response.

        Video processing speed is approximately 1:5.

        Example of detected sports activity:

        ```
        {
          "sport_detected": true,
          "detection_results": [ "shooting goal (soccer)" ],
          "frames": [
              {
                  "label": "shooting goal (soccer)",
                  "frame_number": 98,
                  "confidence": 0.99
              },...
          ]
        }
        ```

        Example response when sports activities were not found:

        ```
        {
          "sport_detected": false,
          "detection_results": []
          "frames": []
        }
        ```

        Please note that the API only provides a set of data (json) about the objects
        found, so no video is generated. The demo video video (above ^) was specially
        created based on json from the API for visual demonstration and better
        perception of the possibilities.

        Args:
          category: AI content moderation with types of sports activity detection

          task_name: Name of the task to be performed

          url: URL to the MP4 file to analyze. File must be publicly accessible via HTTP/HTTPS.

          client_entity_data: Meta parameter, designed to store your own extra information about a video
              entity: video source, video id, etc. It is not used in any way in video
              processing.

              For example, if an AI-task was created automatically when you uploaded a video
              with the AI auto-processing option (nudity detection, etc), then the ID of the
              associated video for which the task was performed will be explicitly indicated
              here.

          client_user_id: Meta parameter, designed to store your own identifier. Can be used by you to tag
              requests from different end-users. It is not used in any way in video
              processing.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["task_name", "url"], ["category", "task_name", "url"])
    async def create(
        self,
        *,
        task_name: Literal["transcription"] | Literal["content-moderation"],
        url: str,
        audio_language: str | Omit = omit,
        client_entity_data: str | Omit = omit,
        client_user_id: str | Omit = omit,
        subtitles_language: str | Omit = omit,
        category: Literal["nsfw"] | Literal["hard_nudity"] | Literal["soft_nudity"] | Literal["sport"] | Omit = omit,
        stop_objects: Literal[
            "ANUS_EXPOSED",
            "BUTTOCKS_EXPOSED",
            "FEMALE_BREAST_EXPOSED",
            "FEMALE_GENITALIA_EXPOSED",
            "MALE_BREAST_EXPOSED",
            "MALE_GENITALIA_EXPOSED",
        ]
        | Literal[
            "ANUS_COVERED",
            "ANUS_EXPOSED",
            "ARMPITS_COVERED",
            "ARMPITS_EXPOSED",
            "BELLY_COVERED",
            "BELLY_EXPOSED",
            "BUTTOCKS_COVERED",
            "BUTTOCKS_EXPOSED",
            "FACE_FEMALE",
            "FACE_MALE",
            "FEET_COVERED",
            "FEET_EXPOSED",
            "FEMALE_BREAST_COVERED",
            "FEMALE_BREAST_EXPOSED",
            "FEMALE_GENITALIA_COVERED",
            "FEMALE_GENITALIA_EXPOSED",
            "MALE_BREAST_EXPOSED",
            "MALE_GENITALIA_EXPOSED",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AITaskCreateResponse:
        return await self._post(
            "/streaming/ai/tasks",
            body=await async_maybe_transform(
                {
                    "task_name": task_name,
                    "url": url,
                    "audio_language": audio_language,
                    "client_entity_data": client_entity_data,
                    "client_user_id": client_user_id,
                    "subtitles_language": subtitles_language,
                    "category": category,
                    "stop_objects": stop_objects,
                },
                ai_task_create_params.AITaskCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AITaskCreateResponse,
        )

    def list(
        self,
        *,
        date_created: str | Omit = omit,
        limit: int | Omit = omit,
        ordering: Literal["task_id", "status", "task_name", "started_at"] | Omit = omit,
        page: int | Omit = omit,
        search: str | Omit = omit,
        status: Literal["FAILURE", "PENDING", "RECEIVED", "RETRY", "REVOKED", "STARTED", "SUCCESS"] | Omit = omit,
        task_id: str | Omit = omit,
        task_name: Literal["transcription", "content-moderation"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AITask, AsyncPageStreamingAI[AITask]]:
        """
        Returns a list of previously created and processed AI tasks.

        The list contains brief information about the task and its execution status.
        Data is displayed page by page.

        Args:
          date_created: Time when task was created. Datetime in ISO 8601 format.

          limit: Number of results to return per page.

          ordering: Which field to use when ordering the results: `task_id`, status, and
              `task_name`. Sorting is done in ascending (ASC) order.

              If parameter is omitted then "started_at DESC" is used for ordering by default.

          page: Page to view from task list, starting from 1

          search: This is an field for combined text search in the following fields: `task_id`,
              `task_name`, status, and `task_data`.

              Both full and partial searches are possible inside specified above fields. For
              example, you can filter tasks of a certain category, or tasks by a specific
              original file.

              Example:

              - To filter tasks of Content Moderation NSFW method:
                `GET /streaming/ai/tasks?search=nsfw`
              - To filter tasks of processing video from a specific origin:
                `GET /streaming/ai/tasks?search=s3.eu-west-1.amazonaws.com`

          status: Task status

          task_id: The task unique identifier to find

          task_name: Type of the AI task. Reflects the original API method that was used to create
              the AI task.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/streaming/ai/tasks",
            page=AsyncPageStreamingAI[AITask],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date_created": date_created,
                        "limit": limit,
                        "ordering": ordering,
                        "page": page,
                        "search": search,
                        "status": status,
                        "task_id": task_id,
                        "task_name": task_name,
                    },
                    ai_task_list_params.AITaskListParams,
                ),
            ),
            model=AITask,
        )

    async def cancel(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AITaskCancelResponse:
        """
        Stopping a previously launched AI-task without waiting for it to be fully
        completed.

        The task will be moved to "REVOKED" status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return await self._post(
            path_template("/streaming/ai/tasks/{task_id}/cancel", task_id=task_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AITaskCancelResponse,
        )

    async def get(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AITaskGetResponse:
        """
        This is the single method to check the execution status of an AI task, and
        obtain the result of any type of AI task.

        Based on the results of processing, the “result” field will contain an answer
        corresponding to the type of the initially created task:

        - ASR: Transcribe video
        - ASR: Translate subtitles
        - CM: Sports detection
        - CM: Not Safe For Work (NSFW) content detection
        - CM: Soft nudity detection
        - CM: Hard nudity detection
        - CM: Objects recognition (soon)
        - etc... (see other methods from /ai/ domain)

        A queue is used to process videos. The waiting time depends on the total number
        of requests in the system, so sometimes you will have to wait.

        Statuses:

        - RECEIVED – the task is accepted by the system
        - PENDING – the task is received and it is pending for available resources
        - STARTED – processing has started
        - SUCCESS – processing has completed successfully
        - FAILURE – processing failed
        - REVOKED – processing was cancelled by the user (or the system)
        - RETRY – the task execution failed due to internal reasons, the task is queued
          for re-execution (up to 3 times)

        Each task is processed in sub-stages, for example, original language is first
        determined in a video, and then transcription is performed. In such cases, the
        video processing status may change from "STARTED" to "PENDING", and back. This
        is due to waiting for resources for a specific processing sub-stage. In this
        case, the overall percentage "progress" of video processing will reflect the
        full picture.

        The result data is stored for 1 month, after which it is deleted.

        For billing conditions see the corresponding methods in /ai/ domain. The task is
        billed only after successful completion of the task and transition to "SUCCESS"
        status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return await self._get(
            path_template("/streaming/ai/tasks/{task_id}", task_id=task_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AITaskGetResponse,
        )

    async def get_ai_settings(
        self,
        *,
        type: Literal["language_support"],
        audio_language: str | Omit = omit,
        subtitles_language: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AITaskGetAISettingsResponse:
        """
        The method for revealing basic information and advanced underlying settings that
        are used when performing AI-tasks.

        Parameter sections:

        - "language_support" – AI Translation: check if a language pair is supported or
          not for AI translation.
        - this list will expand as new AI methods are added.

        **`language_support`**

        There are many languages available for transcription. But not all languages can
        be automatically translated to and from with good quality. In order to determine
        the availability of translation from the audio language to the desired subtitle
        language, you can use this type of "language_support".

        AI models are constantly improving, so this method can be used for dynamic
        determination.

        Example:

        ```
        curl -L 'https://api.gcore.com/streaming/ai/info?type=language_support&audio_language=eng&subtitles_language=fre'

        { "supported": true }
        ```

        Today we provide the following capabilities as below.

        These are the 100 languages for which we support only transcription and
        translation to English. The iso639-2b codes for these are:
        `afr, sqi, amh, ara, hye, asm, aze, bak, eus, bel, ben, bos, bre, bul, mya, cat, zho, hrv, ces, dan, nld, eng, est, fao, fin, fra, glg, kat, deu, guj, hat, hau, haw, heb, hin, hun, isl, ind, ita, jpn, jav, kan, kaz, khm, kor, lao, lat, lav, lin, lit, ltz, mkd, mlg, msa, mal, mlt, mri, mar, ell, mon, nep, nor, nno, oci, pan, fas, pol, por, pus, ron, rus, san, srp, sna, snd, sin, slk, slv, som, spa, sun, swa, swe, tgl, tgk, tam, tat, tel, tha, bod, tur, tuk, ukr, urd, uzb, vie, cym, yid, yor`.

        These are the 77 languages for which we support translation to other languages
        and translation to:
        `afr, amh, ara, hye, asm, aze, eus, bel, ben, bos, bul, mya, cat, zho, hrv, ces, dan, nld, eng, est, fin, fra, glg, kat, deu, guj, heb, hin, hun, isl, ind, ita, jpn, jav, kan, kaz, khm, kor, lao, lav, lit, mkd, mal, mlt, mar, ell, mon, nep, nno, pan, fas, pol, por, pus, ron, rus, srp, sna, snd, slk, slv, som, spa, swa, swe, tgl, tgk, tam, tel, tha, tur, ukr, urd, vie, cym, yor`.

        Args:
          type: The parameters section for which parameters are requested

          audio_language: The source language from which the audio will be transcribed. Required when
              `type=language_support`. Value is 3-letter language code according to ISO-639-2
              (bibliographic code), (e.g., fre for French).

          subtitles_language: The target language the text will be translated into. If omitted, the API will
              return whether the `audio_language` is supported for transcription only, instead
              of translation. Value is 3-letter language code according to ISO-639-2
              (bibliographic code), (e.g., fre for French).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/streaming/ai/info",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "type": type,
                        "audio_language": audio_language,
                        "subtitles_language": subtitles_language,
                    },
                    ai_task_get_ai_settings_params.AITaskGetAISettingsParams,
                ),
            ),
            cast_to=AITaskGetAISettingsResponse,
        )


class AITasksResourceWithRawResponse:
    def __init__(self, ai_tasks: AITasksResource) -> None:
        self._ai_tasks = ai_tasks

        self.create = to_raw_response_wrapper(
            ai_tasks.create,
        )
        self.list = to_raw_response_wrapper(
            ai_tasks.list,
        )
        self.cancel = to_raw_response_wrapper(
            ai_tasks.cancel,
        )
        self.get = to_raw_response_wrapper(
            ai_tasks.get,
        )
        self.get_ai_settings = to_raw_response_wrapper(
            ai_tasks.get_ai_settings,
        )


class AsyncAITasksResourceWithRawResponse:
    def __init__(self, ai_tasks: AsyncAITasksResource) -> None:
        self._ai_tasks = ai_tasks

        self.create = async_to_raw_response_wrapper(
            ai_tasks.create,
        )
        self.list = async_to_raw_response_wrapper(
            ai_tasks.list,
        )
        self.cancel = async_to_raw_response_wrapper(
            ai_tasks.cancel,
        )
        self.get = async_to_raw_response_wrapper(
            ai_tasks.get,
        )
        self.get_ai_settings = async_to_raw_response_wrapper(
            ai_tasks.get_ai_settings,
        )


class AITasksResourceWithStreamingResponse:
    def __init__(self, ai_tasks: AITasksResource) -> None:
        self._ai_tasks = ai_tasks

        self.create = to_streamed_response_wrapper(
            ai_tasks.create,
        )
        self.list = to_streamed_response_wrapper(
            ai_tasks.list,
        )
        self.cancel = to_streamed_response_wrapper(
            ai_tasks.cancel,
        )
        self.get = to_streamed_response_wrapper(
            ai_tasks.get,
        )
        self.get_ai_settings = to_streamed_response_wrapper(
            ai_tasks.get_ai_settings,
        )


class AsyncAITasksResourceWithStreamingResponse:
    def __init__(self, ai_tasks: AsyncAITasksResource) -> None:
        self._ai_tasks = ai_tasks

        self.create = async_to_streamed_response_wrapper(
            ai_tasks.create,
        )
        self.list = async_to_streamed_response_wrapper(
            ai_tasks.list,
        )
        self.cancel = async_to_streamed_response_wrapper(
            ai_tasks.cancel,
        )
        self.get = async_to_streamed_response_wrapper(
            ai_tasks.get,
        )
        self.get_ai_settings = async_to_streamed_response_wrapper(
            ai_tasks.get_ai_settings,
        )
