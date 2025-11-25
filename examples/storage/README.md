# Gcore Storage SDK Examples

This directory contains comprehensive examples demonstrating how to use the Gcore Storage SDK for Python. The examples cover both S3-compatible object storage and SFTP file transfer storage types.

## Directory Structure

The examples are organized into separate files, each with sync and async versions:

```
examples/storage/
├── basic.py              # Sync: Basic storage operations
├── basic_async.py        # Async: Basic storage operations
├── s3_buckets.py         # Sync: S3 bucket management
├── s3_buckets_async.py   # Async: S3 bucket management
├── credentials.py        # Sync: Credential management
├── credentials_async.py  # Async: Credential management
└── README.md             # This file
```

## Available Examples

### 1. Basic Operations (`basic.py` / `basic_async.py`)

Demonstrates fundamental storage operations:
- Creating S3 and SFTP storage instances
- Listing existing storages
- Retrieving storage details
- Updating storage configuration (expiration, server alias)
- Deleting storage instances

**Run the sync example:**
```bash
python examples/storage/basic.py
```

**Run the async example:**
```bash
python examples/storage/basic_async.py
```

**Key Features Demonstrated:**
- Storage creation with different types and locations
- Storage lifecycle management
- Error handling
- Proper credential display at creation time

### 2. S3 Bucket Management (`s3_buckets.py` / `s3_buckets_async.py`)

Comprehensive S3 bucket operations:
- Creating S3 storage instances
- Waiting for storage provisioning
- Creating and managing S3 buckets
- Setting bucket lifecycle policies
- Configuring CORS (Cross-Origin Resource Sharing)
- Managing bucket access policies
- Deleting buckets and cleanup

**Run the sync example:**
```bash
python examples/storage/s3_buckets.py
```

**Run the async example:**
```bash
python examples/storage/s3_buckets_async.py
```

**Key Features Demonstrated:**
- Multiple bucket creation and management
- Lifecycle policy configuration (object expiration)
- CORS policy setup for web applications
- Bucket access policy management (public/private access)
- Proper resource cleanup

### 3. Credentials Management (`credentials.py` / `credentials_async.py`)

Advanced credential management operations:
- S3 access key regeneration
- SFTP password management (generate, set custom, remove)
- Credential security best practices
- Managing multiple storage types simultaneously

**Run the sync example:**
```bash
python examples/storage/credentials.py
```

**Run the async example:**
```bash
python examples/storage/credentials_async.py
```

**Key Features Demonstrated:**
- S3 access and secret key regeneration
- SFTP password lifecycle management
- Disabling/enabling password authentication
- Handling multiple storages in a single example

## Storage Types

### S3-Compatible Storage

Gcore's S3-compatible storage provides:
- **Object Storage**: Store and retrieve files via S3 API
- **Bucket Management**: Create, configure, and manage buckets
- **Access Control**: Set bucket policies and CORS configurations
- **Lifecycle Policies**: Automatic object expiration and cleanup
- **API Compatibility**: Works with existing S3 SDKs and tools

**Use Cases:**
- Web application file storage
- Backup and archival
- Static website hosting
- Content distribution

### SFTP Storage

Gcore's SFTP storage provides:
- **File Transfer**: Standard SFTP protocol for file operations
- **Authentication**: Password and SSH key-based authentication
- **Directory Structure**: Traditional filesystem hierarchy
- **Secure Transfer**: Encrypted file transfers

**Use Cases:**
- Legacy application integration
- Secure file transfers
- Automated backup systems
- FTP replacement

## Configuration

The examples require a Gcore API key to authenticate. Set the `GCORE_API_KEY` environment variable before running any example:

**Linux/macOS:**
```bash
export GCORE_API_KEY=your_api_key_here
```

**Windows (Command Prompt):**
```cmd
set GCORE_API_KEY=your_api_key_here
```

**Windows (PowerShell):**
```powershell
$env:GCORE_API_KEY="your_api_key_here"
```

Alternatively, you can create a `.env` file in the project root with:
```
GCORE_API_KEY=your_api_key_here
```

And load it before running examples (Linux/macOS):
```bash
export $(cat .env | xargs)
```

## Geographic Locations

The examples use specific locations based on storage type:
- **S3 storage**: "s-ed1" (Luxembourg) - supports S3-compatible object storage
- **SFTP storage**: "ams" (Amsterdam) - supports SFTP file transfer

You can change these to any available location that supports your desired storage type. To see available locations, use:

```python
from gcore import Gcore

client = Gcore()
locations = client.storage.locations.list()
for location in locations:
    print(f"{location.code}: {location.name}")
```

## Code Structure

Each example follows a consistent pattern:

- **Main Function**: Orchestrates the example flow by calling individual operation functions
- **Operation Functions**: Each function handles a complete operation (create, list, update, delete, etc.)
- **Keyword-Only Arguments**: All operation functions use keyword-only parameters for clarity
- **Error Handling**: Appropriate error handling and user feedback
- **Printed Output**: Clear section headers and descriptive output for each operation

### Sync vs Async Examples

The SDK provides both synchronous and asynchronous APIs:

**Sync (`Gcore`):**
- Uses `from gcore import Gcore`
- Straightforward, blocking operations
- Easier to understand and debug
- Best for scripts and simple applications

**Async (`AsyncGcore`):**
- Uses `from gcore import AsyncGcore`
- Non-blocking, concurrent operations
- Requires `async`/`await` syntax
- Best for high-performance applications
- Main function uses `asyncio.run(main())`
- Iteration uses `async for` instead of regular `for`

## Troubleshooting

### Common Issues

1. **Storage Creation Failures**
   - Check if location is valid and available
   - Verify storage name is unique and follows naming rules (letters, numbers, dashes, underscores)
   - Ensure API key has proper permissions

2. **Bucket Operation Errors**
   - Ensure storage is S3-compatible (not SFTP)
   - Wait for storage to be fully provisioned before bucket operations (status should be "ok")
   - Bucket names must be unique and follow S3 naming conventions

3. **Authentication Issues**
   - Verify GCORE_API_KEY environment variable is set
   - Check that API key is valid and not expired
   - Ensure API key has permissions for storage operations

4. **Provisioning Timeouts**
   - Storage provisioning can take time, especially for new accounts
   - The examples include a 30-second wait with 2-second intervals
   - If provisioning takes longer, increase max_wait in wait_for_storage_provisioning()

### Getting Help

- Check the [Gcore API Documentation](https://gcore.com/docs/api-reference/storage)
- Review error messages for specific guidance
- Ensure you're using the latest SDK version: `pip install --upgrade gcore`

## Testing on Real Infrastructure

All examples are designed to run on real Gcore infrastructure. They:
- Create real resources (storages, buckets)
- Perform actual API operations
- Include cleanup functions to delete created resources
- Handle errors gracefully to prevent resource leaks

**Important**: Resources created by these examples will incur charges according to your Gcore pricing plan. Always ensure cleanup functions execute successfully to avoid unexpected costs.

## Credentials Security

- Credentials (S3 keys, SFTP passwords) are only visible at creation time and during regeneration operations
- Never commit credentials to version control
- Store credentials securely (e.g., environment variables, secret managers)
- Rotate credentials regularly for security
- Use SSH keys instead of passwords for SFTP when possible

## Python Version

These examples require Python 3.8 or higher, as specified by the SDK requirements.
