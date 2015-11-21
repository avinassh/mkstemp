def is_valid_story_or_comment(form_data):
    parent = form_data.get('parent')
    title = bool(form_data.get('title'))
    url = bool(form_data.get('url'))
    text = bool(form_data.get('text'))
    if parent:
        if title or url:
            return (False, 'Invalid fields for a comment')
        if not text:
            return (False, 'Comment field is missing')
    else:
        if not title:
            return (False, 'Missing title field')
        if text and url:
            return (False, 'Please enter either URL or text, but not both')
    return (True, 'success')
