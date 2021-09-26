using System;
using System.Collections.Generic;
using System.Text;
using RestSharp;
using Jose;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;

namespace Example
{
	class Program
	{
		/// <summary>
		/// This example uses Third-Party libraries RestSharp, Jose and Newtonsoft.Json, all available through NuGet
		/// </summary>

		static void Main(string[] args)
		{
			string jwtTokenString = JwtTokenString();
			Console.WriteLine("Token string: {0}", jwtTokenString);
			List<Object> responses = ApiResponses(jwtTokenString);
			Console.WriteLine("Responses found: {0}", responses.Count);
			Console.ReadLine();
		}

		public static List<Object> ApiResponses(string jwtTokenString)
		{
			var responses = new List<Object>();

			DateTime startDate = new DateTime(2017, 5, 1);
			DateTime endDate = new DateTime(2017, 5, 1, 23, 0, 0);
			string apiEndpoint = String.Format("https://api.stellaconnect.net/v1/data/responses/?start_date={0}&end_date={1}",
												startDate.ToString("yyyy-MM-ddTHH:mm:sszzz"),
												endDate.ToString("yyyy-MM-ddTHH:mm:sszzz"));
			string apiKey = "your-api-key-here";
			var request = new RestRequest(Method.GET);
			request.AddHeader("x-api-key", apiKey);
			request.AddHeader("Authorization", jwtTokenString);

			do
			{
				var client = new RestClient(apiEndpoint);
				IRestResponse response = client.Execute(request);
				var content = JsonConvert.DeserializeObject<Dictionary<string, object>>(response.Content);
				
				JArray newResponses = (JArray)content["responses"];
				for (int i = 0; i < newResponses.Count; i++)
				{
					responses.Add(newResponses[i]);

					// Or do what you'd like here
					var employeeID = newResponses[i]["employee_custom_id"].Value<string>();
					var starRating = newResponses[i]["star_rating"].Value<string>();
				}

				apiEndpoint = content.ContainsKey("next_page") ? (string)content["next_page"] : null;
			}
			while (apiEndpoint != null);

			return responses;
		}

		public static string JwtTokenString()
		{
			byte[] apiSecretKey = Encoding.ASCII.GetBytes("your-api-secret-key-here");
			var payload = new Dictionary<string, object>()
			{
				{ "iat",  CurrentUnixTimestamp() }
			};

			return Jose.JWT.Encode(payload, apiSecretKey, JwsAlgorithm.HS256);
		}

		public static int CurrentUnixTimestamp()
		{
			return (Int32)(DateTime.UtcNow.Subtract(new DateTime(1970, 1, 1))).TotalSeconds;
		}
	}

}