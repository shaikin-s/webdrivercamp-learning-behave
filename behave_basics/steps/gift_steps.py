from behave import *


@step('Navigate to {url}')
def step_impl(context, url):
    context.browser.get(url)
