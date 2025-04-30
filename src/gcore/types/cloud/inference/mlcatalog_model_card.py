# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["MlcatalogModelCard"]


class MlcatalogModelCard(BaseModel):
    id: str
    """
    '#/components/schemas/MLCatalogModelCardSerializerV3/properties/id'
    "$.components.schemas.MLCatalogModelCardSerializerV3.properties.id"
    """

    category: Optional[str] = None
    """
    '#/components/schemas/MLCatalogModelCardSerializerV3/properties/category/anyOf/0'
    "$.components.schemas.MLCatalogModelCardSerializerV3.properties.category.anyOf[0]"
    """

    default_flavor_name: Optional[str] = None
    """
    '#/components/schemas/MLCatalogModelCardSerializerV3/properties/default_flavor_name/anyOf/0'
    "$.components.schemas.MLCatalogModelCardSerializerV3.properties.default_flavor_name.anyOf[0]"
    """

    description: str
    """
    '#/components/schemas/MLCatalogModelCardSerializerV3/properties/description'
    "$.components.schemas.MLCatalogModelCardSerializerV3.properties.description"
    """

    developer: Optional[str] = None
    """
    '#/components/schemas/MLCatalogModelCardSerializerV3/properties/developer/anyOf/0'
    "$.components.schemas.MLCatalogModelCardSerializerV3.properties.developer.anyOf[0]"
    """

    documentation_page: Optional[str] = None
    """
    '#/components/schemas/MLCatalogModelCardSerializerV3/properties/documentation_page/anyOf/0'
    "$.components.schemas.MLCatalogModelCardSerializerV3.properties.documentation_page.anyOf[0]"
    """

    eula_url: Optional[str] = None
    """
    '#/components/schemas/MLCatalogModelCardSerializerV3/properties/eula_url/anyOf/0'
    "$.components.schemas.MLCatalogModelCardSerializerV3.properties.eula_url.anyOf[0]"
    """

    example_curl_request: Optional[str] = None
    """
    '#/components/schemas/MLCatalogModelCardSerializerV3/properties/example_curl_request/anyOf/0'
    "$.components.schemas.MLCatalogModelCardSerializerV3.properties.example_curl_request.anyOf[0]"
    """

    has_eula: bool
    """
    '#/components/schemas/MLCatalogModelCardSerializerV3/properties/has_eula'
    "$.components.schemas.MLCatalogModelCardSerializerV3.properties.has_eula"
    """

    image_registry_id: Optional[str] = None
    """
    '#/components/schemas/MLCatalogModelCardSerializerV3/properties/image_registry_id/anyOf/0'
    "$.components.schemas.MLCatalogModelCardSerializerV3.properties.image_registry_id.anyOf[0]"
    """

    image_url: str
    """
    '#/components/schemas/MLCatalogModelCardSerializerV3/properties/image_url'
    "$.components.schemas.MLCatalogModelCardSerializerV3.properties.image_url"
    """

    inference_backend: Optional[str] = None
    """
    '#/components/schemas/MLCatalogModelCardSerializerV3/properties/inference_backend/anyOf/0'
    "$.components.schemas.MLCatalogModelCardSerializerV3.properties.inference_backend.anyOf[0]"
    """

    inference_frontend: Optional[str] = None
    """
    '#/components/schemas/MLCatalogModelCardSerializerV3/properties/inference_frontend/anyOf/0'
    "$.components.schemas.MLCatalogModelCardSerializerV3.properties.inference_frontend.anyOf[0]"
    """

    api_model_id: Optional[str] = FieldInfo(alias="model_id", default=None)
    """
    '#/components/schemas/MLCatalogModelCardSerializerV3/properties/model_id/anyOf/0'
    "$.components.schemas.MLCatalogModelCardSerializerV3.properties.model_id.anyOf[0]"
    """

    name: str
    """
    '#/components/schemas/MLCatalogModelCardSerializerV3/properties/name'
    "$.components.schemas.MLCatalogModelCardSerializerV3.properties.name"
    """

    openai_compatibility: Optional[str] = None
    """
    '#/components/schemas/MLCatalogModelCardSerializerV3/properties/openai_compatibility/anyOf/0'
    "$.components.schemas.MLCatalogModelCardSerializerV3.properties.openai_compatibility.anyOf[0]"
    """

    port: int
    """
    '#/components/schemas/MLCatalogModelCardSerializerV3/properties/port'
    "$.components.schemas.MLCatalogModelCardSerializerV3.properties.port"
    """

    version: Optional[str] = None
    """
    '#/components/schemas/MLCatalogModelCardSerializerV3/properties/version/anyOf/0'
    "$.components.schemas.MLCatalogModelCardSerializerV3.properties.version.anyOf[0]"
    """
