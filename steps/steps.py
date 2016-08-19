# -*- coding: utf-8 -*-

@given(u'I open (?P<url>.+)')
def step_impl(context, url):
    context.driver.get("http://www.%s/" % url)


@step(u'the title should contain "{title}"')
def step_impl(context, title):
    browser_title = context.driver.title
    assert title in browser_title, 'Found "%s" instead ' % browser_title
