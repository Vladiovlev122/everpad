CONSUMER_KEY = 'nvbn-1422'
CONSUMER_SECRET = 'c17c0979d0054310'
HOST = 'www.evernote.com'
STATUS_NONE = 0
STATUS_SYNC = 1
DEFAULT_SYNC_DELAY = 30000 * 60
SYNC_STATE_START = 0
SYNC_STATE_NOTEBOOKS_LOCAL = 1
SYNC_STATE_TAGS_LOCAL = 2
SYNC_STATE_NOTES_LOCAL = 3
SYNC_STATE_NOTEBOOKS_REMOTE = 4
SYNC_STATE_TAGS_REMOTE = 5
SYNC_STATE_NOTES_REMOTE = 6
SYNC_STATE_FINISH = 7
SYNC_STATES = (
    SYNC_STATE_START, SYNC_STATE_NOTEBOOKS_LOCAL,
    SYNC_STATE_TAGS_LOCAL, SYNC_STATE_NOTES_LOCAL, 
    SYNC_STATE_NOTEBOOKS_REMOTE, SYNC_STATE_TAGS_REMOTE, 
    SYNC_STATE_NOTES_REMOTE, SYNC_STATE_FINISH,
)
DEFAULT_FONT = 'Sans'
DEFAULT_FONT_SIZE = 14
SCHEMA_VERSION = 3
API_VERSION = 3
VERSION = '2.4'
DB_PATH = "~/.everpad/everpad.%s.db" % SCHEMA_VERSION
