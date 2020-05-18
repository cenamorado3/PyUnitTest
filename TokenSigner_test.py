import unittest
from AngularWeb.src.app.WebServer.TokenSigner import TokenSigner
import datetime

class TestTokenSigner(unittest.TestCase):
    def test_TemporalAnomalityDetectorResolve(self):
        signer = TokenSigner()
        x = signer.TemporalAnomality(datetime.datetime.now())
        self.assertFalse(x)

    def test_TemporalAnomalityDetectorReject(self):
        signer = TokenSigner()
        x = signer.TemporalAnomality(datetime.datetime.now() + datetime.timedelta(minutes = -21))
        self.assertTrue(x)

    def test_SignReject(self):
        signer = TokenSigner()
        x = signer.Sign(datetime.datetime.now() + datetime.timedelta(minutes = -21))
        y = 'Etiquette system overload. Resetting now.'
        self.assertEquals(x, y)
        
    def test_SignResolve(self):
        signer = TokenSigner()
        x = signer.Sign(datetime.datetime.now() + datetime.timedelta(minutes = 9))
        y = 'Your decontamination is acknowledged and appreciated. Recommendation: continue efforts to resolve total planetary annihilation.'
        self.assertEquals(x, y)
        
    def test_ParseTime(self):
        signer = TokenSigner()
        x = signer.ParseTime(datetime.datetime.now() + datetime.timedelta(minutes = 9))
        y = [datetime.datetime.now().hour, datetime.datetime.now().minute + 9]
        self.assertEquals(x, y)
    
    
    def test_AddDissonance(self):
        signer = TokenSigner()
        x = signer.AddDissonance(9304340)
        self.assertNotEquals(x, 9304340, msg= 'After Dissonance: {0}'.format(x))
        
if __name__ == '__main__':
    unittest.main()