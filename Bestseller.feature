# Created by noelcanlas at 10/22/22
Feature: # Bestselling count


  Scenario: User see 5 links in Bestseller page
    When Open Amazon Bestseller page
    Then User sees 5 links on page