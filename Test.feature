# -*- coding: utf-8 -*-
# Feature
Feature: Behave Selenium Showcase

Scenario: Open Google and verify the page title is correct
    Given I open "google.com"
    Then the title should contain "Google"

@fails
Scenario: Open wrong page and let the test fail
    Given I open "google-not-found.com"
    Then the title should contain "Google"

