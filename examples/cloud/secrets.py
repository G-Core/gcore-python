from typing import List

from gcore import Gcore
from gcore.types.cloud import Secret
from gcore.types.cloud.secret_upload_tls_certificate_params import Payload


def main() -> None:
    # TODO set API key before running
    # api_key = os.environ["GCORE_API_KEY"]
    # TODO set cloud project ID before running
    # cloud_project_id = os.environ["GCORE_CLOUD_PROJECT_ID"]
    # TODO set cloud region ID before running
    # cloud_region_id = os.environ["GCORE_CLOUD_REGION_ID"]

    client = Gcore(
        # No need to explicitly pass to Gcore constructor if using environment variables
        # api_key=api_key,
        # cloud_project_id=cloud_project_id,
        # cloud_region_id=cloud_region_id,
    )

    cert = upload_tls_certificate_and_poll(client=client)
    get_secret_by_id(client=client, secret_id=cert.id)
    list_all_secrets(client=client)
    delete_secret(client=client, secret_id=cert.id)


def upload_tls_certificate_and_poll(*, client: Gcore) -> Secret:
    print("\n=== UPLOAD TLS CERTIFICATE ===")
    payload = Payload(
        certificate="-----BEGIN CERTIFICATE-----\nMIIFkDCCA3igAwIBAgIUPreVqGwsi0hPOrf8tMK3QMLrRxIwDQYJKoZIhvcNAQEL\nBQAwVTEQMA4GA1UECwwHVW5rbm93bjEQMA4GA1UECgwHVW5rbm93bjEQMA4GA1UE\nBwwHVW5rbm93bjEQMA4GA1UECAwHdW5rbm93bjELMAkGA1UEBhMCQVUwHhcNMjUw\nNDA5MTI1OTQ2WhcNMjUwNTA5MTI1OTQ2WjBrMRQwEgYDVQQDDAtleGFtcGxlLmNv\nbTEQMA4GA1UECwwHVW5rbm93bjEQMA4GA1UECgwHVW5rbm93bjEQMA4GA1UEBwwH\nVW5rbm93bjEQMA4GA1UECAwHdW5rbm93bjELMAkGA1UEBhMCQVUwggIiMA0GCSqG\nSIb3DQEBAQUAA4ICDwAwggIKAoICAQDeVaY8IK93hdmwz7i3eXpY9uN57OPfG0ew\nlsL/rsmwYF+TA45l8E0TnvMgXDRW30D58NUIF+gpLhAXit2M7g0BUDeLVVz8TMcP\ntV+bokyemcEW1ju8oVWi1iW3n+qXjCy9tqyjXZrAbKwdZFvv6fcRQreZlsqbMHlD\nLbcACgtU+HzWJKGzU0rIVOMxj0DQBeDTgN8U70ElhA3ZNqgMTXTwwQtZpZX+Oz9g\nuY+WizNYXHNLD70MEcUtHwg+2tgyBs4mHIQmHb7Dp5OfNM/CwYL+udQuRJjxdG5D\nZor1dXEbVRJdNcas7TfeLHqDOnVF7GUW7OCY6evXTVZFIpu8PFDr48/p0XS71yAu\n4G03S4lQqF2P4H+KplfkGTmdRXccRwaKDsBKljSyrBxi2eiuijmerd4V+qCI6zx8\nUDbxsSm3bFeNtikdVR8Kuhegb3lqT5/nP7FSEoDmxh++i4CcNs35czxTKmPnarov\nD4EnoEH7oDZv2YWoJgDfq6MdO1NMJDUyl6SSeF5MxQY6MyardDKHaXu41USMzrtQ\nN03H3opR+jd7h0IvQAuw6hTjcB5kqAFNT8tpG2wuU1iaJtLHcLICxl6ZU7UANYqn\nQaR53YceKILUCza2rsWriCeC6IVXJbmLo/1dlXYKO2u0gPVGT1rEzMlD8zpkkZFH\nPlhCE+1V9wIDAQABo0IwQDAdBgNVHQ4EFgQUZi0hvSfVSiaiZ958WLgioO0v5jww\nHwYDVR0jBBgwFoAUv5ciSGmtNm2gRbj/E84bSvZwjR4wDQYJKoZIhvcNAQELBQAD\nggIBABd/Idv9TBnQMTGuOZQw1uHvoVpjdsbqYuEEtugmOWeo9wzR6wFVsCg0NJ/e\ncj8fC0PQ3pbZjrRGvBXQLFqzxR2ppSkfiG8aRZiUVxS38b2a9Q2YdvneGdqE5g8C\niZF14c07Bl8gLvHb7BJdUfc8cke/A/KtBQHGuaK6Kj+Ub/XgWut50r8wY9afGg2V\n73VAZOlDAinJo8friikvHIOte1NGCwzapUn8Z0x7ZaNEY5zo1DBZxZgL8XTIcLou\nHVI6Sx5PZhNUR9/QlxtVRM+G29pXSj08TRd6C+ZfWqEIHVWoYBbyWlQy14gQ0c75\nBy2FReHQpwVYAeVh5FFHlFVFO7VEP+cT9/eV3JNin+d5FAn9dXaiuFZLPwqXoQG/\nQoe28un8YXhhzKmpXyU8WORAJuIfR99cZ8EBZ9H/O0tW6tAKyMBXia3f58yHnLCg\nCenmp/T8J2B5V0swffLB3dld+hBfPoQgD9liM+iTWCwelJVKlk0V2q7JoJs+CXzt\nPPCrTwYwj0xuBiZtGkP6LKm+zyhwfMQEpka7N7VrZ6Br+sAzxTyjuu01GedjeWIp\nsLsfRughBJtnkG/Yxf8RMh3akwpoMJjxDF0jlamRrKjilwBcoFmsQZahPMEs67fk\nCf0SW+Q+zKez2y1jhBDvLdm97pvjp5IutcSQB69RAtdUpouO\n-----END CERTIFICATE-----\n",
        certificate_chain="-----BEGIN CERTIFICATE-----\nMIIFizCCA3OgAwIBAgIUGY2OqxQWBvQkvezHv6JjibqgoNEwDQYJKoZIhvcNAQEL\nBQAwVTEQMA4GA1UECwwHVW5rbm93bjEQMA4GA1UECgwHVW5rbm93bjEQMA4GA1UE\nBwwHVW5rbm93bjEQMA4GA1UECAwHdW5rbm93bjELMAkGA1UEBhMCQVUwHhcNMjUw\nNDA5MTI1OTM1WhcNMjUwNTA5MTI1OTM1WjBVMRAwDgYDVQQLDAdVbmtub3duMRAw\nDgYDVQQKDAdVbmtub3duMRAwDgYDVQQHDAdVbmtub3duMRAwDgYDVQQIDAd1bmtu\nb3duMQswCQYDVQQGEwJBVTCCAiIwDQYJKoZIhvcNAQEBBQADggIPADCCAgoCggIB\nAKPOutT9V6/OFjzEU1Q8+U1qTd4ntWCy1OHsopveGyKrPahtsrLY48xvPJklQJJs\naMi5QZje0mNA+Mowuru9WYe8scv0syeNGLyXbmqXhtHNUwh5MfhhOhxkCDjnVHdT\nBVb5grICMWdJzWtSEEAcgAeFwC5UNb99W6pwwIF6N3eaMTbLSm3HCRO8i8kWKw1p\nZcqaNlxyxu7vyFq85t7vyt8m6CkvtEZUKWz2yKZau+A180kVOEViTZBGboGyXWsV\nIopcLOMxWZTbkI69XqMaIQUVr3UTEd5FwR5Rc/GK5ukkfGgpZji+Hj6PGAnCl3Sj\nojRzfpPeJnYA9fepi+JAk+n2tG8/FTp/Hdg1RZ/+NfhRNRi9vzjjbcS/lc164KGg\nqRhk/pmOGTlC1dNYLvJ5O5qrIhz/rhzo1I5PxXaTqTIx/H9RkdnSjkIRu2v6qgZA\nMASayZijLQ+G/dTeXPcU5NQsZyKXQcrVHKviVTxRmJV+UzG+07Uka3IztKFImK9m\nKpW5qcBsVsGgruQyXeg7HVjDgDab6UmDadECpw9eUyNxorIwiRmnrtNLSuWMNznW\n2YgMDXtyByBO9YZrTbmtdbBzFdUIgMhaoEF1P1lrkeSRhP51RdbzndMLuZ/q5uYQ\nzHBXk70O+wmfEwsnEPjuaXFCJPuiYaRFk+GMIBI2liqvAgMBAAGjUzBRMB0GA1Ud\nDgQWBBS/lyJIaa02baBFuP8TzhtK9nCNHjAfBgNVHSMEGDAWgBS/lyJIaa02baBF\nuP8TzhtK9nCNHjAPBgNVHRMBAf8EBTADAQH/MA0GCSqGSIb3DQEBCwUAA4ICAQBG\nYxIeKr1VwkhYh3eDOUsUXx1NNCwNmpOM6LNsRIKO1Z4CKLrjsuYNgSNuPlUietN7\nS60l+j1b9i/oQvKN0YkZAm6Pe/zUJ8NMg11Ussd09ysDbjG2jjc6GXM08neK8TcO\nKYEbml2OVVlE8q+R2EYocdH2GnLwLwjheLU17Hh2tqrlG5QnUTUZQsB55MXMKldP\nAiiPI1sWo4p7XOoCQvyWo0Q1FVQM8XhxzxkvDYilBGGy1Sq3auZ3aOFR9BZeCEIk\n0EgXV94v1PhHZGV4JpzkOwEOTQ3EUAwS1/01jdYwXaxu5vI08dwZMTZg31aMXyfp\n33T5wqZVyqkGmX8jrqmPFCjGJxb/0ZI7uWG8RtjS1XcBPdjq6JPYwVMT0HFhxnOQ\nq5hBeq1dcunFBWPAjXl//qdRMVCuHKfEGBWUoFmpF5C0cBVeR+JSRzn2WSm3Nqet\n/4P2ICu95MIXDidmigdJCkF8vZ9MVwMU6Zk6Bx0Gd/qPwkbEVe89gMsbIKVUzZPV\nTP8iDwdzb4DXsZSZyQaJcYPhLddY9WIInf524/GjpMJSdsIRdKuqISJySvsCID9E\ns+0EYjsjWCc+KLqvQB+AXgZqDtrPFwTQDOLyhaps9dkrBt0CFNN6HP3CTvACiPpm\n4GH/L4MCmbUR6m6oFnd6SXNFJwUETYv3N6iCl/chiw==\n-----END CERTIFICATE-----\n-----BEGIN CERTIFICATE-----\nMIIFizCCA3OgAwIBAgIUGY2OqxQWBvQkvezHv6JjibqgoNEwDQYJKoZIhvcNAQEL\nBQAwVTEQMA4GA1UECwwHVW5rbm93bjEQMA4GA1UECgwHVW5rbm93bjEQMA4GA1UE\nBwwHVW5rbm93bjEQMA4GA1UECAwHdW5rbm93bjELMAkGA1UEBhMCQVUwHhcNMjUw\nNDA5MTI1OTM1WhcNMjUwNTA5MTI1OTM1WjBVMRAwDgYDVQQLDAdVbmtub3duMRAw\nDgYDVQQKDAdVbmtub3duMRAwDgYDVQQHDAdVbmtub3duMRAwDgYDVQQIDAd1bmtu\nb3duMQswCQYDVQQGEwJBVTCCAiIwDQYJKoZIhvcNAQEBBQADggIPADCCAgoCggIB\nAKPOutT9V6/OFjzEU1Q8+U1qTd4ntWCy1OHsopveGyKrPahtsrLY48xvPJklQJJs\naMi5QZje0mNA+Mowuru9WYe8scv0syeNGLyXbmqXhtHNUwh5MfhhOhxkCDjnVHdT\nBVb5grICMWdJzWtSEEAcgAeFwC5UNb99W6pwwIF6N3eaMTbLSm3HCRO8i8kWKw1p\nZcqaNlxyxu7vyFq85t7vyt8m6CkvtEZUKWz2yKZau+A180kVOEViTZBGboGyXWsV\nIopcLOMxWZTbkI69XqMaIQUVr3UTEd5FwR5Rc/GK5ukkfGgpZji+Hj6PGAnCl3Sj\nojRzfpPeJnYA9fepi+JAk+n2tG8/FTp/Hdg1RZ/+NfhRNRi9vzjjbcS/lc164KGg\nqRhk/pmOGTlC1dNYLvJ5O5qrIhz/rhzo1I5PxXaTqTIx/H9RkdnSjkIRu2v6qgZA\nMASayZijLQ+G/dTeXPcU5NQsZyKXQcrVHKviVTxRmJV+UzG+07Uka3IztKFImK9m\nKpW5qcBsVsGgruQyXeg7HVjDgDab6UmDadECpw9eUyNxorIwiRmnrtNLSuWMNznW\n2YgMDXtyByBO9YZrTbmtdbBzFdUIgMhaoEF1P1lrkeSRhP51RdbzndMLuZ/q5uYQ\nzHBXk70O+wmfEwsnEPjuaXFCJPuiYaRFk+GMIBI2liqvAgMBAAGjUzBRMB0GA1Ud\nDgQWBBS/lyJIaa02baBFuP8TzhtK9nCNHjAfBgNVHSMEGDAWgBS/lyJIaa02baBF\nuP8TzhtK9nCNHjAPBgNVHRMBAf8EBTADAQH/MA0GCSqGSIb3DQEBCwUAA4ICAQBG\nYxIeKr1VwkhYh3eDOUsUXx1NNCwNmpOM6LNsRIKO1Z4CKLrjsuYNgSNuPlUietN7\nS60l+j1b9i/oQvKN0YkZAm6Pe/zUJ8NMg11Ussd09ysDbjG2jjc6GXM08neK8TcO\nKYEbml2OVVlE8q+R2EYocdH2GnLwLwjheLU17Hh2tqrlG5QnUTUZQsB55MXMKldP\nAiiPI1sWo4p7XOoCQvyWo0Q1FVQM8XhxzxkvDYilBGGy1Sq3auZ3aOFR9BZeCEIk\n0EgXV94v1PhHZGV4JpzkOwEOTQ3EUAwS1/01jdYwXaxu5vI08dwZMTZg31aMXyfp\n33T5wqZVyqkGmX8jrqmPFCjGJxb/0ZI7uWG8RtjS1XcBPdjq6JPYwVMT0HFhxnOQ\nq5hBeq1dcunFBWPAjXl//qdRMVCuHKfEGBWUoFmpF5C0cBVeR+JSRzn2WSm3Nqet\n/4P2ICu95MIXDidmigdJCkF8vZ9MVwMU6Zk6Bx0Gd/qPwkbEVe89gMsbIKVUzZPV\nTP8iDwdzb4DXsZSZyQaJcYPhLddY9WIInf524/GjpMJSdsIRdKuqISJySvsCID9E\ns+0EYjsjWCc+KLqvQB+AXgZqDtrPFwTQDOLyhaps9dkrBt0CFNN6HP3CTvACiPpm\n4GH/L4MCmbUR6m6oFnd6SXNFJwUETYv3N6iCl/chiw==\n-----END CERTIFICATE-----\n",
        private_key="-----BEGIN PRIVATE KEY-----\n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\nkf90Czon6WsRXM2o++kWrtXIa8IR\n-----END PRIVATE KEY-----\n",
    )
    secret = client.cloud.secrets.upload_tls_certificate_and_poll(name="gcore-python-example", payload=payload)
    print(f"Secret ID: {secret.id}, name: {secret.name}")
    print("========================")
    return secret


def get_secret_by_id(*, client: Gcore, secret_id: str) -> Secret:
    print("\n=== GET SECRET BY ID ===")
    secret = client.cloud.secrets.get(secret_id=secret_id)
    print(f"Secret ID: {secret.id}, name: {secret.name}")
    print("========================")
    return secret


def list_all_secrets(*, client: Gcore) -> List[Secret]:
    print("\n=== LIST ALL SECRETS ===")
    all_secrets = client.cloud.secrets.list()
    for count, secret in enumerate(all_secrets, 1):
        print(f"  {count}. Secret ID: {secret.id}, name: {secret.name}")
    print("========================")
    return all_secrets.results


def delete_secret(*, client: Gcore, secret_id: str) -> None:
    print("\n=== DELETE SECRET ===")
    client.cloud.secrets.delete(secret_id=secret_id)
    print(f"Secret deleted successfully: {secret_id}")
    print("========================")


if __name__ == "__main__":
    main()
