import time
import asyncio

from gcore import AsyncGcore
from gcore.types.cdn import CaCertificate
from gcore.pagination import AsyncOffsetPage

# A self-signed CA certificate generated solely for this example. It contains
# only the public certificate (no private key), so it is safe to commit.
# Trusted CA certificates are used to verify the origin when CDN connects to it
# over HTTPS.
TEST_CA_CERTIFICATE_PEM = """-----BEGIN CERTIFICATE-----
MIIDYzCCAkugAwIBAgIUNt315IS68yUNhQvSV+qPme7huXgwDQYJKoZIhvcNAQEL
BQAwQTEiMCAGA1UEAwwZR2NvcmUgU0RLIEV4YW1wbGUgVGVzdCBDQTEbMBkGA1UE
CgwSR2NvcmUgU0RLIEV4YW1wbGVzMB4XDTI2MDUxOTE1NTMyOFoXDTM2MDUxNjE1
NTMyOFowQTEiMCAGA1UEAwwZR2NvcmUgU0RLIEV4YW1wbGUgVGVzdCBDQTEbMBkG
A1UECgwSR2NvcmUgU0RLIEV4YW1wbGVzMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8A
MIIBCgKCAQEAt/rXbgO4GtT+t3utz6YrcsF1rRdYYxlVjtSEsbsfw7sz1IElprT1
w9+Q3n4fmg0OaEF6yQWr9K0+SUiXWgFS9twaYFRUe6M8PANLAwyoWe0BT7gqkq3n
pF53uy0CuFE0HybC/3oiGpQeVvYDUtEr9I+c/rHwbSOPXSvJ8c86HqHCxNrxB21Q
8GDHBE47Er5LVbam6Cs8MG9nT5T10TkClDRckxoxCOcTX14Nf1Me+MTcDehcZ/mZ
vViVFNUaeTCTd9YXoZK1ok8YXDeD8hfGYsHsrHVhdLNYpXWo54DodnNvevw5ilXl
7bQ67WA8e2hpY01Odt/xUZQ9IRZs7lxsjwIDAQABo1MwUTAdBgNVHQ4EFgQU+exr
mFzjx+K9muACuEFypkxi3fkwHwYDVR0jBBgwFoAU+exrmFzjx+K9muACuEFypkxi
3fkwDwYDVR0TAQH/BAUwAwEB/zANBgkqhkiG9w0BAQsFAAOCAQEATTwh2j7DbF0v
4JOrSTaLUtWo7ugcy1H2nepA0aagZWNqoMDUmY3RLbgbz7HKBWS1lqjSJRQR8bRo
8qmSTbLYfX/NgERAcAgyv9UoGaTH3g5diCgr6jgy+t5qpRE4YNW0rWOO1RuE0/ly
U3tgSULD1n24IWLAQeLpz9ADZvXCZofBopuysro8yGvvz2BreqLAjFy8jTuPOoae
71/nXhQ+ycoxSZShJ5yIip4R8hTBPMBuIb3aLD/hNVO8qIl07DX7FrWQPiTaLZrF
KI0T0vo3PB1rEcmAQl/lNwbnIkyZMOYmGFi9FA01Uvf6QPi9u0GC+4NxWUHJjLju
mNIQqB91Uw==
-----END CERTIFICATE-----"""


async def main() -> None:
    # TODO set API key before running
    # api_key = os.environ["GCORE_API_KEY"]

    gcore = AsyncGcore(
        # No need to explicitly pass to AsyncGcore constructor if using environment variables
        # api_key=api_key,
    )

    certificate = await create_trusted_ca_certificate(client=gcore)
    await list_trusted_ca_certificates(client=gcore)
    assert certificate.id is not None
    await get_trusted_ca_certificate(client=gcore, certificate_id=certificate.id)
    await delete_trusted_ca_certificate(client=gcore, certificate_id=certificate.id)


async def create_trusted_ca_certificate(*, client: AsyncGcore) -> CaCertificate:
    print("\n=== CREATE TRUSTED CA CERTIFICATE ===")
    # The certificate name must be unique, so use a timestamp suffix.
    name = f"gcore-python-example-ca-{int(time.time())}"
    certificate = await client.cdn.trusted_ca_certificates.create(
        name=name,
        ssl_certificate=TEST_CA_CERTIFICATE_PEM,
    )
    print(
        f"Created Trusted CA Certificate: ID={certificate.id}, "
        f"name={certificate.name}, issuer={certificate.cert_issuer}"
    )
    print("=====================================")
    return certificate


async def list_trusted_ca_certificates(*, client: AsyncGcore) -> AsyncOffsetPage[CaCertificate]:
    print("\n=== LIST TRUSTED CA CERTIFICATES ===")
    result = await client.cdn.trusted_ca_certificates.list()
    count = 0
    async for certificate in result:
        count += 1
        print(f"  {count}. Trusted CA Certificate: ID={certificate.id}, name={certificate.name}")
    print("====================================")
    return result


async def get_trusted_ca_certificate(*, client: AsyncGcore, certificate_id: int) -> CaCertificate:
    print("\n=== GET TRUSTED CA CERTIFICATE ===")
    certificate = await client.cdn.trusted_ca_certificates.get(certificate_id)
    print(
        f"Trusted CA Certificate: ID={certificate.id}, name={certificate.name}, "
        f"subject_cn={certificate.cert_subject_cn}, valid_until={certificate.validity_not_after}"
    )
    print("==================================")
    return certificate


async def delete_trusted_ca_certificate(*, client: AsyncGcore, certificate_id: int) -> None:
    print("\n=== DELETE TRUSTED CA CERTIFICATE ===")
    await client.cdn.trusted_ca_certificates.delete(certificate_id)
    print(f"Deleted Trusted CA Certificate: ID={certificate_id}")
    print("=====================================")


if __name__ == "__main__":
    asyncio.run(main())
