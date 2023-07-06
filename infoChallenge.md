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
    Content struct {
        Level uint `json:"Level"`
        Challenge struct {
            Username string `json:"Username"`
            Secret string `json:"Secret"`
            Points uint `json:"Points"`
        } `json:"Challenge"`
        Protocol string `json:"Protocol"`
        SecretKey string `json:"SecretKey"`
    } `json:"Content"`
}


Here is your first Challenge: 
61c132fc7995138d1094de0b70bb89fe6ca0edca
f8bd836156e994a49004c3f253f8aad5f9d3177d
Don't forget that: 800ab01c158d4271e7f366203666a6b7eb6e4535

CopyTrash cSfXHMvB T75f91DQ2C
App ID : 724490 --> Jeu Protocol sur Steam
Tiny ctf esgi 5A
Q DC3 ) 1 4
