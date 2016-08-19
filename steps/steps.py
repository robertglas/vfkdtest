# -*- coding: utf-8 -*-

@given(u'I open google.com')
def step_impl(context):
    context.driver.get("http://www.google.com/")


@step(u'the title should contain "{title}"')
def step_impl(context, title):
    browser_title = context.driver.title
    assert title in browser_title, 'Found "%s" instead ' % browser_title
