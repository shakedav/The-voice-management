import { TheVoiceUiPage } from './app.po';

describe('the-voice-ui App', () => {
  let page: TheVoiceUiPage;

  beforeEach(() => {
    page = new TheVoiceUiPage();
  });

  it('should display welcome message', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('Welcome to app!!');
  });
});
