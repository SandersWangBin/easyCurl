#!/usr/bin/python

# KEYWORDS
KEYWORD_URL = 'URL'
KEYWORD_METHOD = 'METHOD'
KEYWORD_HEADERS = 'HEADERS'
KEYWORD_BODY = 'BODY'
KEYWORD_CONTROL = 'CONTROL'
KEYWORD_EXPECT = 'EXPECT'
KEYWORD_RC = 'RESTCASES'
KEYWORD_TC = 'TESTCASES'

# URL for FOR ALL CASES
URL       = 'http://easyCurl.com/test/objs'
URL_OBJ01 = 'http://easyCurl.com/test/objs/myObj01'
URL_OBJ02 = 'http://easyCurl.com/test/objs/myObj02'

# REST METHOD FOR ALL OF CASES
METHOD_POST   = 'POST'
METHOD_GET    = 'GET'
METHOD_DELETE = 'DELETE'
METHOD_PUT    = 'PUT'

# REQUEST HEADERS FOR ALL OF CASES
HEADERS = ['Content-Type: application/json;charset=UTF-8', 'Accept: application/json']

# REQUEST BODY FOR ALL OF CASES
BODY_POST_OBJ01  = '{"id":"myObj","description":" the obj created for testing purpose","version":"0.0.1","validity":true}'
BODY_PUT_OBJ02   = '{"description":" the second obj created for testing purpose","version":"0.0.1","validity":true}'
BODY_EMPTY       = ''

# CONTROL INFO FOR GET TC
CONTROL_GET = 'LOOP:2, DELAY:1'

# EXPECT INFO FOR RESPONSE
EXPECT_20X = 'STATUSCODE:201|200'

# REST CASES
RC_POST_OBJ01   = {KEYWORD_URL:URL,       KEYWORD_METHOD:METHOD_POST,   KEYWORD_HEADERS:HEADERS, KEYWORD_BODY:BODY_POST_OBJ01, KEYWORD_EXPECT:EXPECT_20X}
RC_PUT_OBJ02    = {KEYWORD_URL:URL_OBJ02, KEYWORD_METHOD:METHOD_PUT,    KEYWORD_HEADERS:HEADERS, KEYWORD_BODY:BODY_PUT_OBJ02,  KEYWORD_EXPECT:EXPECT_20X}
RC_GET          = {KEYWORD_URL:URL,       KEYWORD_METHOD:METHOD_GET,    KEYWORD_HEADERS:HEADERS, KEYWORD_BODY:BODY_EMPTY,      KEYWORD_EXPECT:EXPECT_20X}
RC_DELETE_OBJ01 = {KEYWORD_URL:URL_OBJ01, KEYWORD_METHOD:METHOD_DELETE, KEYWORD_HEADERS:HEADERS, KEYWORD_BODY:BODY_EMPTY,      KEYWORD_EXPECT:EXPECT_20X}
RC_DELETE_OBJ02 = {KEYWORD_URL:URL_OBJ02, KEYWORD_METHOD:METHOD_DELETE, KEYWORD_HEADERS:HEADERS, KEYWORD_BODY:BODY_EMPTY,      KEYWORD_EXPECT:EXPECT_20X}

# TEST CASES
TC_CREATE_DELETE = {'TC_CREATE_DELETE': {KEYWORD_RC:[RC_POST_OBJ01, RC_PUT_OBJ02, RC_GET, RC_DELETE_OBJ01, RC_DELETE_OBJ02]}}
TC_GET_NULL = {'TC_GET_NULL': {KEYWORD_RC:[RC_GET], KEYWORD_CONTROL:CONTROL_GET}}

# TEST SUITE (THE VARIABLE NAME OF TEST SUITE SHOULD BE EASYCURL_TESTSUITE
# OTHERWISE THE EASYCURL COULD NOT RECOGNIZE
EASYCURL_TESTSUITE = {'TS_ECOBJ_01': {KEYWORD_TC:[TC_GET_NULL, TC_CREATE_DELETE, TC_GET_NULL]}}