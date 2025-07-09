#!/bin/bash

RESULT_GET=$(curl --request GET http://127.0.0.1:5000/api/timeline_post)
echo "GET result: $RESULT_GET"

RESULT_POST=$(curl -X POST -F name=pertulio -F email=pertulio@mail.com -F content='Proin vulputate, lectus non blandit pellentesque, arcu leo gravida quam, vitae ornare mi ex eu mauris. Quisque ultrices, massa sit amet luctus varius, mi ipsum rutrum neque, id blandit odio nunc sed metus. Sed eget aliquet mauris. Duis ut erat convallis odio egestas laoreet eu sed mi.' http://127.0.0.1:5000/api/timeline_post)

echo "POST result: $RESULT_POST"

POST_ID=$(echo "$RESULT_POST" | grep -o '"id":[ ]*[0-9]*' | head -1 | grep -o '[0-9]*')

RESULT_DELETE=$(curl -X DELETE http://127.0.0.1:5000/api/timeline_post/$POST_ID)
echo "DELETE result: $RESULT_DELETE"