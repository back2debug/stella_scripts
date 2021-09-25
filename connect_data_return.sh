#!/bin/bash
# Your API key is 
# Your Secret for request signing is 
# You may execute this script (assuming you have npm installed) to make an example request
# from the Stella Data API.

# To integrate your internal services, use the provided documentation at
# and a library from http://jwt.io in your system language, to be able to generate a JSON Web Token (jwt).
# Set your token in the get request header for each seperate request made as in the curl request below:
# "Authorization: ${TOKEN}"
#
# This header is in addition to the "x-api-key" header you've previously used for the Requests Post API,
# that is used to submit new feedback requests.

# You may execute this script to generate example tokens and make example requests from any Linux or Mac
# machine (or from a Windows VM) which has `curl` and `node`/`npm` installed via the terminal;
# simply run this file with bash like so: `bash connect_data_return.sh`

# The start date and end date are configurable ISO8601 date-times. The below request uses the
# prior 24 hour UTC period at the time this file was generated.

# check if jwtgen is installed
which jwtgen
JWTGEN_PRESENT=$?
if [[ $JWTGEN_PRESENT != 0 ]]; then
  # go ahead and install jwtgen
  npm install -g jwtgen
fi

# set keys and secret in the environment
export API_KEY=
export SECRET=

# generate and set the token in the environment, including iat (issued at) time of generation as UTC unix timestamp.
# this token will be valid for up to 24 hours, though you may also specify exp (expiration time) for a shorter validity window
export TOKEN=`jwtgen -a "HS256" -s ${SECRET}`

# print token
echo $TOKEN

# Token consists of base64 encoded metadata about signature, a base 64 encoded "claim", and a signature of the claim
PARTS=(${TOKEN//./ })
METADATA=${PARTS[0]}
CLAIM=${PARTS[1]}
SIGNATURE=${PARTS[2]} #not base64 encoded json, just base64 of raw binary HMAC of claim and secret
echo "Encoded Token Metadata:"
echo $METADATA
echo "Decoded Token Metadata:"
echo $METADATA | base64 -D
echo
echo "Encoded Token Claim:"
echo $CLAIM
echo "Decoded Token Claim:"
echo $CLAIM | base64 -D
echo
echo "HMAC Signature:"
echo $SIGNATURE
echo "Making request to Stella Connect with x-api-key and Authorization/token headers:"

# execute curl to retrieve data.
curl -v "https://api.stellaconnect.net/production/data/responses?start_date=2018-10-09T00:00:00Z&end_date=2018-10-10T00:00:00Z" -H "x-api-key: ${API_KEY}" -H "Authorization: ${TOKEN}"