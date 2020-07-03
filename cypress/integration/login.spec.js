/// <reference types="cypress" />

context('Login', () => {
  beforeEach(() => {
    Cypress.Cookies.debug(true);
    Cypress.Cookies.preserveOnce('ipm-token');
  })

  it('Go home', () => {
    cy.visit('http://localhost:4200/login');
  });

  it('type wrong username', () => {
    cy.get('#username').type('1234username').should('have.value', '1234username');
  });

  it('type wrong password', () => {
    cy.get('#password').type('1234password').should('have.value', '1234password');
  });

  it('perform wrong login', () => {
    cy.clearCookie('ipm-token');
    cy.contains('Login').click();
    cy.wait(2000);
  });

  it('check feedback', () => {
    cy.get('mat-card-footer').contains('Login failed, please try again');
  });

  it('get token from backend and store it in cookies', () => {
    cy.request({
      url: 'http://localhost:5000/login',
      headers: {
        'Authorization': 'Basic YWRtaW46YWRtaW4='
      }
    })
    .then((response) => {
      expect(response).property('status').to.equal(200)
      expect(response).property('body').to.include.keys('token')

      cy.setCookie('ipm-token', response.body.token);
    });

  });

  it('check cookie', () => {
    cy.getCookie('ipm-token').should('be.not.equal', null);
  });

})
