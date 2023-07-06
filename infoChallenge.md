GET 10.33.2.123:${PORT}/ping

${PORT} : 1024 --> 4096

## Available Routes

PATH                METHOD          BODY
/ping               GET
/signup             POST            {"User" : "xxxx"}
/check              POST            {"User" : "xxxx"}
/secret             POST            {"User" : "xxxx"}

/getLevel           POST            AuthRequest
/getUserPoints      POST            AuthRequest
/getChallenge       POST            AuthRequest

/getHint            POST            AuthRequest
/submitChallenge    POST            FullRequest

User : Lutenruto
My secret : b10157a56ed0aeb2b0c84912ca11ec480050bff7c2a07f9af3a7131e822bbb29

Request struct {
    User string `json:"User"`
}

AuthRequest struct {
    User string `json:"User"`
    Secret string `json:"Secret"`
}

FullRequest struct {
    User string `json:"User"`
    Secret string `json:"Secret"`
    Content ? `json:"Content"`
}