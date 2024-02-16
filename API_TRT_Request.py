{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "equal-smith",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{\"script\": [{\"ObjectName\": \"M32\", \"StationName\": \"SRO\", \"RA\": \"05:35:17.29\", \"DEC\": \"-05:23:27.9\", \"BinningXY\": \"1,1\", \"CadenceInterval\": \"00:00:00\", \"MaxAirmass\": \"3\", \"PA\": \"0\", \"Dither\": \"0\", \"ExpiryDate\": \"2021-07-31 16:11:21\", \"StartDate\": \"2021-06-20 16:11:21\", \"EndDate\": \"2021-06-26 16:11:21\", \"ExposuresMode\": \"1\", \"M3Port\": \"1\", \"Filter\": [\"B\", \"V\", \"R\", \"I\"], \"Suffix\": [\"M32_B\", \"M32_V\", \"M32_R\", \"M32_I\"], \"Exposure\": [\"120\", \"120\", \"120\", \"120\"], \"Repeat\": [\"5\", \"5\", \"5\", \"5\"]}]} \n",
      "\n"
     ]
    },
    {
     "ename": "MissingSchema",
     "evalue": "Invalid URL 'Enter Your API address': No scheme supplied. Perhaps you meant https://Enter Your API address?",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mMissingSchema\u001b[0m                             Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[3], line 38\u001b[0m\n\u001b[1;32m     33\u001b[0m \u001b[38;5;28mprint\u001b[39m(payload, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m)\n\u001b[1;32m     34\u001b[0m headers \u001b[38;5;241m=\u001b[39m {\n\u001b[1;32m     35\u001b[0m               \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mContent-Type\u001b[39m\u001b[38;5;124m'\u001b[39m: \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mapplication/json\u001b[39m\u001b[38;5;124m'\u001b[39m,\n\u001b[1;32m     36\u001b[0m               \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mTRT\u001b[39m\u001b[38;5;124m'\u001b[39m: \u001b[38;5;124m'\u001b[39m\u001b[38;5;124meyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZDk0MTdhNzQzNzUxYzBmNmNiZGRjMjAiLCJuYW1lIjoiS2FudGhhbmFrb3JuIE5veXNlbmEiLCJncm91cElkIjoxLCJncm91cE5hbWUiOiJyZXNlYXJjaGVyIiwicHJpb3JpdHlJZCI6IjY1OGFjYmJlMDhhYmY2MDI3ODNhMGFjOCIsInByaW9yaXR5Ijo5NSwic3RhcnREYXRlIjoiMjAyNC0wMS0wMVQwMDowMTowMC4wMDBaIiwiZXhwaXJlRGF0ZSI6IjIwMjQtMDQtMzBUMjM6NTk6MDAuMDAwWiIsImlhdCI6MTcwNDk1ODkwMiwiZXhwIjoxNzE0NDYyOTAyfQ.v9bQFhmrThw5sCpD1OAlpHWQa3v_v10EgeIuTxge2yE\u001b[39m\u001b[38;5;124m'\u001b[39m\n\u001b[1;32m     37\u001b[0m           }\n\u001b[0;32m---> 38\u001b[0m response \u001b[38;5;241m=\u001b[39m \u001b[43mrequests\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mrequest\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mPOST\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43murl\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mheaders\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mheaders\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mdata\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mpayload\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m     39\u001b[0m keep_id\u001b[38;5;241m.\u001b[39mappend(response\u001b[38;5;241m.\u001b[39mtext)\n\u001b[1;32m     40\u001b[0m \u001b[38;5;28mprint\u001b[39m(response\u001b[38;5;241m.\u001b[39mtext)\n",
      "File \u001b[0;32m/lustre/GOTOML/kanthanakorn/conda/envs/goto/lib/python3.12/site-packages/requests/api.py:59\u001b[0m, in \u001b[0;36mrequest\u001b[0;34m(method, url, **kwargs)\u001b[0m\n\u001b[1;32m     55\u001b[0m \u001b[38;5;66;03m# By using the 'with' statement we are sure the session is closed, thus we\u001b[39;00m\n\u001b[1;32m     56\u001b[0m \u001b[38;5;66;03m# avoid leaving sockets open which can trigger a ResourceWarning in some\u001b[39;00m\n\u001b[1;32m     57\u001b[0m \u001b[38;5;66;03m# cases, and look like a memory leak in others.\u001b[39;00m\n\u001b[1;32m     58\u001b[0m \u001b[38;5;28;01mwith\u001b[39;00m sessions\u001b[38;5;241m.\u001b[39mSession() \u001b[38;5;28;01mas\u001b[39;00m session:\n\u001b[0;32m---> 59\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43msession\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mrequest\u001b[49m\u001b[43m(\u001b[49m\u001b[43mmethod\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mmethod\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43murl\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43murl\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43mkwargs\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[0;32m/lustre/GOTOML/kanthanakorn/conda/envs/goto/lib/python3.12/site-packages/requests/sessions.py:575\u001b[0m, in \u001b[0;36mSession.request\u001b[0;34m(self, method, url, params, data, headers, cookies, files, auth, timeout, allow_redirects, proxies, hooks, stream, verify, cert, json)\u001b[0m\n\u001b[1;32m    562\u001b[0m \u001b[38;5;66;03m# Create the Request.\u001b[39;00m\n\u001b[1;32m    563\u001b[0m req \u001b[38;5;241m=\u001b[39m Request(\n\u001b[1;32m    564\u001b[0m     method\u001b[38;5;241m=\u001b[39mmethod\u001b[38;5;241m.\u001b[39mupper(),\n\u001b[1;32m    565\u001b[0m     url\u001b[38;5;241m=\u001b[39murl,\n\u001b[0;32m   (...)\u001b[0m\n\u001b[1;32m    573\u001b[0m     hooks\u001b[38;5;241m=\u001b[39mhooks,\n\u001b[1;32m    574\u001b[0m )\n\u001b[0;32m--> 575\u001b[0m prep \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mprepare_request\u001b[49m\u001b[43m(\u001b[49m\u001b[43mreq\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    577\u001b[0m proxies \u001b[38;5;241m=\u001b[39m proxies \u001b[38;5;129;01mor\u001b[39;00m {}\n\u001b[1;32m    579\u001b[0m settings \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mmerge_environment_settings(\n\u001b[1;32m    580\u001b[0m     prep\u001b[38;5;241m.\u001b[39murl, proxies, stream, verify, cert\n\u001b[1;32m    581\u001b[0m )\n",
      "File \u001b[0;32m/lustre/GOTOML/kanthanakorn/conda/envs/goto/lib/python3.12/site-packages/requests/sessions.py:486\u001b[0m, in \u001b[0;36mSession.prepare_request\u001b[0;34m(self, request)\u001b[0m\n\u001b[1;32m    483\u001b[0m     auth \u001b[38;5;241m=\u001b[39m get_netrc_auth(request\u001b[38;5;241m.\u001b[39murl)\n\u001b[1;32m    485\u001b[0m p \u001b[38;5;241m=\u001b[39m PreparedRequest()\n\u001b[0;32m--> 486\u001b[0m \u001b[43mp\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mprepare\u001b[49m\u001b[43m(\u001b[49m\n\u001b[1;32m    487\u001b[0m \u001b[43m    \u001b[49m\u001b[43mmethod\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mrequest\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mmethod\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mupper\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m    488\u001b[0m \u001b[43m    \u001b[49m\u001b[43murl\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mrequest\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43murl\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m    489\u001b[0m \u001b[43m    \u001b[49m\u001b[43mfiles\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mrequest\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mfiles\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m    490\u001b[0m \u001b[43m    \u001b[49m\u001b[43mdata\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mrequest\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mdata\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m    491\u001b[0m \u001b[43m    \u001b[49m\u001b[43mjson\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mrequest\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mjson\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m    492\u001b[0m \u001b[43m    \u001b[49m\u001b[43mheaders\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mmerge_setting\u001b[49m\u001b[43m(\u001b[49m\n\u001b[1;32m    493\u001b[0m \u001b[43m        \u001b[49m\u001b[43mrequest\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mheaders\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mheaders\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mdict_class\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mCaseInsensitiveDict\u001b[49m\n\u001b[1;32m    494\u001b[0m \u001b[43m    \u001b[49m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m    495\u001b[0m \u001b[43m    \u001b[49m\u001b[43mparams\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mmerge_setting\u001b[49m\u001b[43m(\u001b[49m\u001b[43mrequest\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mparams\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mparams\u001b[49m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m    496\u001b[0m \u001b[43m    \u001b[49m\u001b[43mauth\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mmerge_setting\u001b[49m\u001b[43m(\u001b[49m\u001b[43mauth\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mauth\u001b[49m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m    497\u001b[0m \u001b[43m    \u001b[49m\u001b[43mcookies\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mmerged_cookies\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m    498\u001b[0m \u001b[43m    \u001b[49m\u001b[43mhooks\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mmerge_hooks\u001b[49m\u001b[43m(\u001b[49m\u001b[43mrequest\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mhooks\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mhooks\u001b[49m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m    499\u001b[0m \u001b[43m\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    500\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m p\n",
      "File \u001b[0;32m/lustre/GOTOML/kanthanakorn/conda/envs/goto/lib/python3.12/site-packages/requests/models.py:368\u001b[0m, in \u001b[0;36mPreparedRequest.prepare\u001b[0;34m(self, method, url, headers, files, data, params, auth, cookies, hooks, json)\u001b[0m\n\u001b[1;32m    365\u001b[0m \u001b[38;5;250m\u001b[39m\u001b[38;5;124;03m\"\"\"Prepares the entire request with the given parameters.\"\"\"\u001b[39;00m\n\u001b[1;32m    367\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mprepare_method(method)\n\u001b[0;32m--> 368\u001b[0m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mprepare_url\u001b[49m\u001b[43m(\u001b[49m\u001b[43murl\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mparams\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    369\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mprepare_headers(headers)\n\u001b[1;32m    370\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mprepare_cookies(cookies)\n",
      "File \u001b[0;32m/lustre/GOTOML/kanthanakorn/conda/envs/goto/lib/python3.12/site-packages/requests/models.py:439\u001b[0m, in \u001b[0;36mPreparedRequest.prepare_url\u001b[0;34m(self, url, params)\u001b[0m\n\u001b[1;32m    436\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m InvalidURL(\u001b[38;5;241m*\u001b[39me\u001b[38;5;241m.\u001b[39margs)\n\u001b[1;32m    438\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m scheme:\n\u001b[0;32m--> 439\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m MissingSchema(\n\u001b[1;32m    440\u001b[0m         \u001b[38;5;124mf\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mInvalid URL \u001b[39m\u001b[38;5;132;01m{\u001b[39;00murl\u001b[38;5;132;01m!r}\u001b[39;00m\u001b[38;5;124m: No scheme supplied. \u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[1;32m    441\u001b[0m         \u001b[38;5;124mf\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mPerhaps you meant https://\u001b[39m\u001b[38;5;132;01m{\u001b[39;00murl\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m?\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[1;32m    442\u001b[0m     )\n\u001b[1;32m    444\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m host:\n\u001b[1;32m    445\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m InvalidURL(\u001b[38;5;124mf\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mInvalid URL \u001b[39m\u001b[38;5;132;01m{\u001b[39;00murl\u001b[38;5;132;01m!r}\u001b[39;00m\u001b[38;5;124m: No host supplied\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n",
      "\u001b[0;31mMissingSchema\u001b[0m: Invalid URL 'Enter Your API address': No scheme supplied. Perhaps you meant https://Enter Your API address?"
     ]
    }
   ],
   "source": [
    "# Observation scheduling on TRT through an API request.\n",
    "\n",
    "# API address\n",
    "import requests\n",
    "import json\n",
    "\n",
    "url = \"Enter Your API address\"\n",
    "keep_id = []\n",
    "\n",
    "#Example for script observation to input parameters\n",
    "script= dict([(\"ObjectName\", \"M32\"),                                                                                                 \n",
    "                (\"StationName\", \"SRO\"),                                                                                              \n",
    "                (\"RA\", \"05:35:17.29\"),                                                     \n",
    "                (\"DEC\", \"-05:23:27.9\"),                                                   \n",
    "                (\"BinningXY\", \"1,1\"),                                                                                                \n",
    "                (\"CadenceInterval\", \"00:00:00\"),                                                                                     \n",
    "                (\"MaxAirmass\", \"3\"),                                                                                                 \n",
    "                (\"PA\", \"0\"),                                                                                                         \n",
    "                (\"Dither\", \"0\"),                                                                                                     \n",
    "                (\"ExpiryDate\", \"2021-07-31 16:11:21\"),                                                                            \n",
    "                (\"StartDate\", \"2021-06-20 16:11:21\"),                                                                      \n",
    "                (\"EndDate\", \"2021-06-26 16:11:21\"),                                                                               \n",
    "                (\"ExposuresMode\", \"1\"),                                                                                              \n",
    "                (\"M3Port\", \"1\"),                                                                                                     \n",
    "                (\"Filter\", [\"B\", \"V\", \"R\", \"I\"]),                                                                                    \n",
    "                (\"Suffix\", [\"M32_B\", \"M32_V\", \"M32_R\", \"M32_I\"]),      \n",
    "                (\"Exposure\", [\"120\",\"120\",\"120\", \"120\"]),                                                                            \n",
    "                (\"Repeat\", [\"5\",\"5\",\"5\", \"5\"])                                                                                       \n",
    "              ])\n",
    "\n",
    "# Convert text to Json format\n",
    "payload = json.dumps({\"script\": [ script] })\n",
    "print(payload, \"\\n\")\n",
    "headers = {\n",
    "              'Content-Type': 'application/json',\n",
    "              'TRT': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZDk0MTdhNzQzNzUxYzBmNmNiZGRjMjAiLCJuYW1lIjoiS2FudGhhbmFrb3JuIE5veXNlbmEiLCJncm91cElkIjoxLCJncm91cE5hbWUiOiJyZXNlYXJjaGVyIiwicHJpb3JpdHlJZCI6IjY1OGFjYmJlMDhhYmY2MDI3ODNhMGFjOCIsInByaW9yaXR5Ijo5NSwic3RhcnREYXRlIjoiMjAyNC0wMS0wMVQwMDowMTowMC4wMDBaIiwiZXhwaXJlRGF0ZSI6IjIwMjQtMDQtMzBUMjM6NTk6MDAuMDAwWiIsImlhdCI6MTcwNDk1ODkwMiwiZXhwIjoxNzE0NDYyOTAyfQ.v9bQFhmrThw5sCpD1OAlpHWQa3v_v10EgeIuTxge2yE'\n",
    "          }\n",
    "response = requests.request(\"POST\", url, headers=headers, data=payload)\n",
    "keep_id.append(response.text)\n",
    "print(response.text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "approved-script",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:conda-goto]",
   "language": "python",
   "name": "conda-env-conda-goto-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
