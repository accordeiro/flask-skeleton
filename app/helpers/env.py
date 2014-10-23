import json, os, re, sys

# Helper Functions
def load_env(paths=[]):
    def set_env_vars(content=''):
        for line in content.splitlines():
            matched_env_var = re.match(r'\A([A-Za-z_0-9]+)=(.*)\Z', line)
            if matched_env_var:
                key, val = matched_env_var.group(1), matched_env_var.group(2)
                m2 = re.match(r"\A'(.*)'\Z", val)
                if m2:
                    val = m2.group(1)
                m3 = re.match(r'\A"(.*)"\Z', val)
                if m3:
                    val = re.sub(r'\\(.)', r'\1', m3.group(1))
                os.environ.setdefault(key, val)

    for path in paths:
        try:
            with open(path) as f:
                content = f.read()
                set_env_vars(content=content)
        except IOError:
            print "WARNING: Could not load environment variables from %s. This should be ok for production." % path


def env_get(var_name, default=None):
    return os.environ.get(var_name, default)
