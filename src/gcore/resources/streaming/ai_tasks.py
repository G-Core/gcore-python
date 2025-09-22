# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
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

    def create(
        self,
        *,
        task_name: Literal["transcription", "content-moderation"],
        url: str,
        audio_language: str | Omit = omit,
        category: Literal["sport", "nsfw", "hard_nudity", "soft_nudity"] | Omit = omit,
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

        - Create an AI task, specify algoritm to use
        - Get `task_id`
        - Check a result using `.../ai/tasks/{task_id}` method

        For more detailed information, see the description of each method separately.

        **AI Automatic Speech Recognition (ASR)**

        AI is instrumental in automatic video processing for subtitles creation by using
        Automatic Speech Recognition (ASR) technology to transcribe spoken words into
        text, which can then be translated into multiple languages for broader
        accessibility.

        Categories:

        - `transcription` – to create subtitles/captions from audio in the original
          language.
        - `translation` – to transate subtitles/captions from the original language to
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
        - `hard_nudity`: Detailed analisys of video which detects explicit nudity
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

        - It's allowed to analyse still images too (where applicable). Format of image:
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
                "detection_results": ["nsfw"],
                "frames": [{"label": "nsfw", "confidence": 1.0, "frame_number": 24}, ...],
            },
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

        Args:
          task_name: Name of the task to be performed

          url: URL to the MP4 file to analyse. File must be publicly accessible via HTTP/HTTPS.

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

          category: Model for analysis (content-moderation only). Determines what exactly needs to
              be found in the video.

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

          subtitles_language: Indicates which language it is clearly necessary to translate into. If this is
              not set, the original language will be used from attribute "`audio_language`".

              Please note that:

              - transcription into the original language is a free procedure,
              - and translation from the original language into any other languages is a
                "translation" procedure and is paid. More details in
                [POST /streaming/ai/tasks#transcribe](/docs/api-reference/streaming/ai/create-ai-asr-task).
                Language is set by 3-letter language code according to ISO-639-2
                (bibliographic code).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/streaming/ai/tasks",
            body=maybe_transform(
                {
                    "task_name": task_name,
                    "url": url,
                    "audio_language": audio_language,
                    "category": category,
                    "client_entity_data": client_entity_data,
                    "client_user_id": client_user_id,
                    "subtitles_language": subtitles_language,
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

              If parameter is omitted then "`started_at` DESC" is used for ordering by
              default.

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

          task_id: The task unique identifier to fiund

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
            f"/streaming/ai/tasks/{task_id}/cancel",
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
            f"/streaming/ai/tasks/{task_id}",
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

        - "`language_support`" – AI Translation: check if a language pair is supported
          or not for AI translation.
        - this list will expand as new AI methods are added.

        **`language_support`**

        There are many languages available for transcription. But not all languages can
        be automatically translated to and from with good quality. In order to determine
        the availability of translation from the audio language to the desired subtitle
        language, you can use this type of "`language_support`".

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

    async def create(
        self,
        *,
        task_name: Literal["transcription", "content-moderation"],
        url: str,
        audio_language: str | Omit = omit,
        category: Literal["sport", "nsfw", "hard_nudity", "soft_nudity"] | Omit = omit,
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

        - Create an AI task, specify algoritm to use
        - Get `task_id`
        - Check a result using `.../ai/tasks/{task_id}` method

        For more detailed information, see the description of each method separately.

        **AI Automatic Speech Recognition (ASR)**

        AI is instrumental in automatic video processing for subtitles creation by using
        Automatic Speech Recognition (ASR) technology to transcribe spoken words into
        text, which can then be translated into multiple languages for broader
        accessibility.

        Categories:

        - `transcription` – to create subtitles/captions from audio in the original
          language.
        - `translation` – to transate subtitles/captions from the original language to
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
        - `hard_nudity`: Detailed analisys of video which detects explicit nudity
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

        - It's allowed to analyse still images too (where applicable). Format of image:
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
                "detection_results": ["nsfw"],
                "frames": [{"label": "nsfw", "confidence": 1.0, "frame_number": 24}, ...],
            },
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

        Args:
          task_name: Name of the task to be performed

          url: URL to the MP4 file to analyse. File must be publicly accessible via HTTP/HTTPS.

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

          category: Model for analysis (content-moderation only). Determines what exactly needs to
              be found in the video.

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

          subtitles_language: Indicates which language it is clearly necessary to translate into. If this is
              not set, the original language will be used from attribute "`audio_language`".

              Please note that:

              - transcription into the original language is a free procedure,
              - and translation from the original language into any other languages is a
                "translation" procedure and is paid. More details in
                [POST /streaming/ai/tasks#transcribe](/docs/api-reference/streaming/ai/create-ai-asr-task).
                Language is set by 3-letter language code according to ISO-639-2
                (bibliographic code).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/streaming/ai/tasks",
            body=await async_maybe_transform(
                {
                    "task_name": task_name,
                    "url": url,
                    "audio_language": audio_language,
                    "category": category,
                    "client_entity_data": client_entity_data,
                    "client_user_id": client_user_id,
                    "subtitles_language": subtitles_language,
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

              If parameter is omitted then "`started_at` DESC" is used for ordering by
              default.

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

          task_id: The task unique identifier to fiund

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
            f"/streaming/ai/tasks/{task_id}/cancel",
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
            f"/streaming/ai/tasks/{task_id}",
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

        - "`language_support`" – AI Translation: check if a language pair is supported
          or not for AI translation.
        - this list will expand as new AI methods are added.

        **`language_support`**

        There are many languages available for transcription. But not all languages can
        be automatically translated to and from with good quality. In order to determine
        the availability of translation from the audio language to the desired subtitle
        language, you can use this type of "`language_support`".

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
