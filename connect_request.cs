using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

// Import the REST Client Libraries
using IO.Swagger.Client;
using IO.Swagger.Model;
using IO.Swagger.Api;

namespace ConnectAPIExample
{
    class Example
    {
        static void Main(string[] args)
        {
            // Build our api key pair
            string apiKey = "yourapikeyhere";
            Dictionary<string, string> keyPair = new Dictionary<string, string>();
            keyPair.Add("x-api-key", apiKey);

            // Build out the client
            Configuration config = new Configuration(apiKey: keyPair);
            RequestApi client = new RequestApi(config);

            // Build the feedback request
            RequestCustomer customer = new RequestCustomer();
            customer.Email = "customer@fakedomain.com";
            customer.Name = "Customer Name";

            RequestEmployee employee = new RequestEmployee();
            employee.Email = "agent@fakedomain.com";

            Request request = new Request();
            request.Customer = customer;
            request.Employee = employee;
            request.Channel = "phone";

            // Send out the request and record our request id
            InlineResponse200 result = client.Request(request);
            string requestId = result.RequestId;
        }
    }
}