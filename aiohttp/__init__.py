__version__ = '4.0.0a0'

from typing import Tuple  # noqa

from . import hdrs
from .client import (
    BaseConnector,
    ClientConnectionError,
    ClientConnectorCertificateError,
    ClientConnectorError,
    ClientConnectorSSLError,
    ClientError,
    ClientHttpProxyError,
    ClientOSError,
    ClientPayloadError,
    ClientProxyConnectionError,
    ClientRequest,
    ClientResponse,
    ClientResponseError,
    ClientSession,
    ClientSSLError,
    ClientTimeout,
    ClientWebSocketResponse,
    ContentTypeError,
    Fingerprint,
    InvalidURL,
    NamedPipeConnector,
    RequestInfo,
    ServerConnectionError,
    ServerDisconnectedError,
    ServerFingerprintMismatch,
    ServerTimeoutError,
    TCPConnector,
    TooManyRedirects,
    UnixConnector,
    WSServerHandshakeError,
    request,
)
from .cookiejar import CookieJar, DummyCookieJar
from .formdata import FormData
from .helpers import BasicAuth, ChainMapProxy
from .http import (
    HttpVersion,
    HttpVersion10,
    HttpVersion11,
    WebSocketError,
    WSCloseCode,
    WSMessage,
    WSMsgType,
)
from .multipart import (
    BadContentDispositionHeader,
    BadContentDispositionParam,
    BodyPartReader,
    MultipartReader,
    MultipartWriter,
    content_disposition_filename,
    parse_content_disposition,
)
from .payload import (
    PAYLOAD_REGISTRY,
    AsyncIterablePayload,
    BufferedReaderPayload,
    BytesIOPayload,
    BytesPayload,
    IOBasePayload,
    JsonPayload,
    Payload,
    StringIOPayload,
    StringPayload,
    TextIOPayload,
    get_payload,
    payload_type,
)
from .resolver import AsyncResolver, DefaultResolver, ThreadedResolver
from .signals import Signal
from .streams import (
    EMPTY_PAYLOAD,
    DataQueue,
    EofStream,
    FlowControlDataQueue,
    StreamReader,
)
from .tracing import (
    TraceConfig,
    TraceConnectionCreateEndParams,
    TraceConnectionCreateStartParams,
    TraceConnectionQueuedEndParams,
    TraceConnectionQueuedStartParams,
    TraceConnectionReuseconnParams,
    TraceDnsCacheHitParams,
    TraceDnsCacheMissParams,
    TraceDnsResolveHostEndParams,
    TraceDnsResolveHostStartParams,
    TraceRequestChunkSentParams,
    TraceRequestEndParams,
    TraceRequestExceptionParams,
    TraceRequestRedirectParams,
    TraceRequestStartParams,
    TraceResponseChunkReceivedParams,
)

__all__ = (
    'hdrs',
    # client
    'BaseConnector',
    'ClientConnectionError',
    'ClientConnectorCertificateError',
    'ClientConnectorError',
    'ClientConnectorSSLError',
    'ClientError',
    'ClientHttpProxyError',
    'ClientOSError',
    'ClientPayloadError',
    'ClientProxyConnectionError',
    'ClientResponse',
    'ClientRequest',
    'ClientResponseError',
    'ClientSSLError',
    'ClientSession',
    'ClientTimeout',
    'ClientWebSocketResponse',
    'ContentTypeError',
    'Fingerprint',
    'InvalidURL',
    'RequestInfo',
    'ServerConnectionError',
    'ServerDisconnectedError',
    'ServerFingerprintMismatch',
    'ServerTimeoutError',
    'TCPConnector',
    'TooManyRedirects',
    'UnixConnector',
    'NamedPipeConnector',
    'WSServerHandshakeError',
    'request',
    # cookiejar
    'CookieJar',
    'DummyCookieJar',
    # formdata
    'FormData',
    # helpers
    'BasicAuth',
    'ChainMapProxy',
    # http
    'HttpVersion',
    'HttpVersion10',
    'HttpVersion11',
    'WSMsgType',
    'WSCloseCode',
    'WSMessage',
    'WebSocketError',
    # multipart
    'BadContentDispositionHeader',
    'BadContentDispositionParam',
    'BodyPartReader',
    'MultipartReader',
    'MultipartWriter',
    'content_disposition_filename',
    'parse_content_disposition',
    # payload
    'AsyncIterablePayload',
    'BufferedReaderPayload',
    'BytesIOPayload',
    'BytesPayload',
    'IOBasePayload',
    'JsonPayload',
    'PAYLOAD_REGISTRY',
    'Payload',
    'StringIOPayload',
    'StringPayload',
    'TextIOPayload',
    'get_payload',
    'payload_type',
    # resolver
    'AsyncResolver',
    'DefaultResolver',
    'ThreadedResolver',
    # signals
    'Signal',
    # streams
    'DataQueue',
    'EMPTY_PAYLOAD',
    'EofStream',
    'FlowControlDataQueue',
    'StreamReader',
    # tracing
    'TraceConfig',
    'TraceConnectionCreateEndParams',
    'TraceConnectionCreateStartParams',
    'TraceConnectionQueuedEndParams',
    'TraceConnectionQueuedStartParams',
    'TraceConnectionReuseconnParams',
    'TraceDnsCacheHitParams',
    'TraceDnsCacheMissParams',
    'TraceDnsResolveHostEndParams',
    'TraceDnsResolveHostStartParams',
    'TraceRequestChunkSentParams',
    'TraceRequestEndParams',
    'TraceRequestExceptionParams',
    'TraceRequestRedirectParams',
    'TraceRequestStartParams',
    'TraceResponseChunkReceivedParams',
)  # type: Tuple[str, ...]

try:
    from .worker import GunicornWebWorker, GunicornUVLoopWebWorker  # noqa
    __all__ += ('GunicornWebWorker', 'GunicornUVLoopWebWorker')
except ImportError:  # pragma: no cover
    pass
