#!/bin/bash

set -eux

SERVERS=`mktemp`
OUTPUT=`mktemp`

cat > "$SERVERS" << EOF
[
    {
        "HOST": "foo",
        "VLAN": "1"
    },
    {
        "HOST": "bar",
        "VLAN": "1"
    },
]
EOF

lock-set-database $SERVERS

lock-get-database > $OUTPUT
diff $OUTPUT - << EOF
[{   'HOST': 'foo', 'VLAN': '1'}, {   'HOST': 'bar', 'VLAN': '1'}]
EOF

lock-list > $OUTPUT
diff $OUTPUT /dev/null

lock-get-server-by-host foo > $OUTPUT
grep "HOST=foo" $OUTPUT
grep "LOCK=" $OUTPUT

eval `grep "LOCK=" $OUTPUT`

lock-list > $OUTPUT
grep "$LOCK" $OUTPUT

lock-release $LOCK

lock-list > $OUTPUT
diff $OUTPUT /dev/null

lock-get-single-server > $OUTPUT
grep "LOCK=" $OUTPUT
grep "VLAN=1" $OUTPUT
grep "HOST=foo" $OUTPUT

eval `grep "LOCK=" $OUTPUT`
lock-release $LOCK

lock-get-server-pair > $OUTPUT
grep "HOST0=foo" $OUTPUT
grep "HOST1=bar" $OUTPUT
