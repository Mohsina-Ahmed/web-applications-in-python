# Tests for your routes go here

# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"

"""
When I make a GET request to /
Then: I should get a 200 response
"""
def test_get_wave(web_client):
    response = web_client.get('/wave?name=Dana')
    #Assert that the status code was 200 (OK)
    assert response.status_code == 200

    #Assert that the data returned was the right string
    assert response.data.decode('utf-8') ==  'I am waving at Dana'

"""
When: I make a POST request to /submit
And: I send a name and message as body parameters
Then: I should get a 200 response with the right content
"""
def test_post_submit(web_client):
    # We will simulate sending a POST request to /submit wiht a name and message
    # This returns a response object we can test against.
    response = web_client.post('/submit', data={'name': 'Dana', 'message': 'Hello'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Thanks Dana, you sent this message: "Hello"'

"""
When: I make a POST request to /count_vowels
And: I send "eee" as the body parameter text
Then: I should get a 200 response with 3 in the message
"""

def test_post_count_vowels_eee(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eee'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 3 vowels in "eee"'

"""
When: I make a POST request to /count_vowels
And: I send "eunoia" as the body parameter text
Then: I should get a 200 response with 5 in the message
"""
def test_post_count_vowels_eunoia(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eunoia'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 5 vowels in "eunoia"'

"""
When: I make a POST request to /count_vowels
And: I send "mercurial" as the body parameter text
Then: I should get a 200 response with 4 in the message
"""
def test_post_count_vowels_mercurial(web_client):
    response = web_client.post('/count_vowels', data={'text': 'mercurial'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 4 vowels in "mercurial"'

# EXAMPLE

# POST /sort-names
# with names=Joe,Alice,Zoe,Julia,Kieran
# Expected response (200 OK):
"""
Joe,Alice,Zoe,Julia,Kieran
"""

def test_post_sort_names_with_a_list_of_names(web_client):
    response = web_client.post('/sort-names', data={'names': 'Joe,Alice,Zoe,Julia,Kieran'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice,Joe,Julia,Kieran,Zoe'

# POST /sort-names
# with names=Aaaaaa,Aaaaaz,Aaaaab
# Expected response (200 OK):
"""
Aaaaaa,Aaaaaz,Aaaaab
"""
def test_post_sort_names_with_a_list_of_names_with_letters_at_the_end(web_client):
    response = web_client.post('/sort-names', data={'names': 'Aaaaaa,Aaaaaz,Aaaaab'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Aaaaaa,Aaaaab,Aaaaaz'


# POST /sort-names
# with no names
# Expected response Invalid Request:
"""
You did not submit any names as response
"""



"""
When: I make a POST request to /sort-names
And: I send [''] as the body parameter list
Then: I should a 400 response with a sorted list in alphabetical order ['Aliah', 'Maria', 'Sarah'] 
"""

def test_post_sort_with_empty_text(web_client):
    #response = web_client.post('/sort-names', data={'names': ''})
    response = web_client.post('/sort-names')
    assert response.status_code == 400
    assert response.data.decode('utf-8') == "Please provide a list of strings (comma-seperated)"

# POST /add-names
# list: 'Joe,Alice,Julia,Kieran,Zoe'
# with a name 'Mohsina'
# Expected response as 'Alice,Joe,Julia,Kieran,Mohsina,Zoe'
"""
'Alice,Joe,Julia,Kieran,Mohsina,Zoe'
"""
def test_post_add_a_name_in_a_list(web_client):
    response = web_client.post('/add-names', data={'names': 'Joe,Alice,Julia,Kieran,Zoe'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice,Joe,Julia,Kieran,Mohsina,Zoe'


# === End Example Code ===
