GET 10.33.2.123:3210/ping

${PORT} : 1024 --> 65535

## Available Routes

PATH            METHOD          BODY
/ping           Get
/signup         POST            {"User" : "xxxx"}
/check          POST            {"User" : "xxxx"}
/secret         POST            {"User" : "xxxx"}

User : Lutenruto
My secret : b10157a56ed0aeb2b0c84912ca11ec480050bff7c2a07f9af3a7131e822bbb29

Request struct {
    User string `json:"User"`
}

Response struct {
    User string `json:"User"`
    Secret string `json:"Secret"`
}