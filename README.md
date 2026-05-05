# Stella Connect Integration Scripts

Example scripts for integrating with the Stella Connect API across multiple languages. Covers the two main APIs: **Requests** (submitting feedback requests) and **Data Return** (retrieving response data). The company has since been acquired by UKG.

---

## Scripts

### Submitting Feedback Requests

| File | Language | Description |
|------|----------|-------------|
| `connect_request.sh` | Bash | POST a feedback request via curl |
| `connect_request.cs` | C# | Submit a request using the Swagger-generated client |
| `connect_request_vba.txt` | VBA | Submit requests from an Excel spreadsheet |
| `connect_requests_from_file.py` | Python | Bulk-submit requests by reading rows from a CSV file |
| `connect_service_recovery_request.py` | Python | Submit a service recovery follow-up request |

### Retrieving Response Data

| File | Language | Description |
|------|----------|-------------|
| `connect_data_return.sh` | Bash | Fetch response data using JWT auth via curl |
| `data_return.cs` | C# | Paginated data retrieval with JWT auth |
| `connect_data_return_zendesk.py` | Python | Pull response data and push star ratings/comments onto Zendesk tickets; auto-creates service recovery tickets for low ratings |

---

## Authentication

**Requests API** uses an `x-api-key` header.

**Data Return API** uses both `x-api-key` and a JWT `Authorization` header. The JWT is signed with your secret using HS256 and should include an `iat` (issued at) claim.

```python
import jwt, datetime
token = jwt.encode({'iat': datetime.datetime.now()}, YOUR_SECRET, algorithm='HS256')
headers = {'x-api-key': YOUR_API_KEY, 'Authorization': token}
```

---

## Configuration

Each script has clearly marked placeholders at the top. At minimum, set:

- `API_KEY` — your Stella Connect API key
- `SECRET` — your signing secret (Data Return scripts only)

For `connect_requests_from_file.py`, prepare a CSV (`filename.csv`) with columns:
`Customer Name`, `Customer's Email Address`, `Agent Email`, `Channel`, `SR Number`

For `connect_data_return_zendesk.py`, also set:
- Your Zendesk subdomain in the `UPDATE_TKT_URL` / `CREATE_TKT_URL` constants
- Your Zendesk API token and user in `USER` / `PWD`
- Your custom field IDs for star rating, comments, and request ID
