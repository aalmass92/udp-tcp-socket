import subprocess

def run_cmd(cmd):
    """Helper to run shell commands and print output/errors."""
    print(f"\n>>> Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr)
    return result

# 1. Generate server private key
run_cmd("openssl genrsa -out server.key 2048")

# 2. Create CSR using the private key
run_cmd('openssl req -new -key server.key -out server.csr -subj "/C=CA/ST=Alberta/L=Calgary/O=ahmed/OU=DataComm/CN=project.local"')

# 3. Verify CSR information
run_cmd("openssl req -text -in server.csr -noout -verify")

# 4. Self-sign the certificate with server key
run_cmd("openssl x509 -in server.csr -out server.crt -req -signkey server.key -days 365")

# 6. Verify certificate information
run_cmd("openssl x509 -text -in server.crt -noout")

# 7. Confirm keys match (hash comparison)
run_cmd("openssl pkey -pubout -in server.key | openssl sha256")
run_cmd("openssl req -pubkey -in server.csr -noout | openssl sha256")
run_cmd("openssl x509 -pubkey -in server.crt -noout | openssl sha256")

print("\nCertificate creation workflow complete. Files generated: server.key, server.csr, server.crt")
