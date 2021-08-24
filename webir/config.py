# Default configuration file, distributed in the application package

# The name of the LIRC remote managed by this WebIR instance
REMOTE_NAME = 'Telefunken-LCD-TV'

# Map of supported channel names to the corresponding channel number on the managed TV
CHANNELS = {
    "televisión española": 825,
    "la 1": 825,
    "la uno": 825,
    "la 2": 826,
    "la dos": 826,
    "antena 3": 831,
    "antena tres": 831,
    "cuatro": 805,
    "telecinco": 804,
    "la sexta": 832,
    "telemadrid": 835,
    "teledeporte": 849,
    "tdp": 849,
    "neox": 833,
    "24h": 827,
    "24 horas": 827,
    "dmax": 819
}

AUTH_JWKS_URL = "http://localhost:8081/auth/realms/home/protocol/openid-connect/certs"
AUTH_ISSUER = "http://localhost:8081/auth/realms/home"
AUTH_AUDIENCE = "webir-alexa"
AUTH_SCOPE = "webir"
