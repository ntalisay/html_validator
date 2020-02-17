#!/bin/python3


def validate_html(html):
    '''
    This function performs a limited version of html validation by checking whether every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''
    tag_lst = _extract_tags(html)
    l = []
    i = 0
    balanced = True
    for i in range(len(tag_lst)):
        head = tag_lst[i]
        
        if head[1] != '/': 
            l.push(tag_lst)
        else: 
            if l == []:
                balanced = False
            else:
                top = l.pop() 
                if top[1:] != head[2:] :
                    balanced = False

    if balanced and s == []:
        return True
    else:
        return False


    # HINT:
    # use the _extract_tags function below to generate a list of html tags without any extra text;
    # then process these html tags using the balanced parentheses algorithm from the book
    # the main difference between your code and the book's code will be that you will have to keep track of not just the 3 types of parentheses,
    # but arbitrary text located between the html tags


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not meant to be used directly by the user are prefixed with an underscore.

    This function returns a list of all the html tags contained in the input string,
    stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''

    tags = []
    l = ""
    for i in range(len(html)):
        string_ind = html[i]
        if string_ind  == '<':
            n = 0
            while string_ind != '>' :
                l += l + html[i + 1]
                n += 1
            l += ">"
            tags.append(tags)
            l = ""

    return tags
