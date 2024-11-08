from wmain.api import WBaidu_Netdisk
from pprint import pprint

# share_uk:"1100586214790", shareid:"41767244614"

# TEST
if __name__ == "__main__":
    bd = WBaidu_Netdisk()
    bd.session.ini.set_proxy(7890)
    bd.login(
        """ndut_fmt=F0D4A5E509EF8A06201901531C42C81A0C178BDC77010E3CD1073132B95BCE75;BAIDUID=4A4B0253B183C6721BA485642DB2CD72:FG=1;BDUSS_BFESS=WxPaWE5S0xQNVBNbmJHNTVia2tldUtPd2cxVTBpUmJwczhsc0ZzY3QzMW8yd2huRVFBQUFBJCQAAAAAAAAAAAEAAACuhdCQMTIzxOPU2jEyMTM4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGhO4WZoTuFmS;BAIDU_WISE_UID=wapp_1725863321661_326;__bid_n=191cca2d7314032d3cb6ac;PANWEB=1;ZFY=93QJeNpnOYiDWXOaWnfOoLLVf2BTaUDApZJszxXPJ84:C;XFI=247a3c4d-09d2-ca94-d206-45ff09b9a3a4;ab_sr=1.0.1_ZjBiMDE3MjE2MWJiZDUxYjQ1ZmQyNzViNzU5NjM5ODJkNTVlZjBlNzA4NmFkZWY0MDE4MjI2MDRkZWEyZDAxMTlkNzUyMWQ1OWMyMjE2OWYyYzZkODU3ODA2MGJlMTNlNjIwMDc2MDFjYjQwOGVkNTU2NWVmODViMmJkYjA2YWFjYjU1Mzc4ZDA2MGExYzQwYWZlNjRkMDRjOGFkNjVhMjkzMzZkZjg5ZDlkMDYwMzZhNDhmODJiNjNlMDY5NDYw;BAIDUID_BFESS=4A4B0253B183C6721BA485642DB2CD72:FG=1;STOKEN=985849c5b19601574751e258393cf0028d5a8022609d4a181d976b5b6fbbde6a;newlogin=1;BIDUPSID=4A4B0253B183C6721BA485642DB2CD72;BDCLND=r0kP39%2B9MhGlkTRZ60qfXD7HQysi0HQ5lVC%2Frwc0HNw%3D;BDORZ=FAE1F8CFA4E8841CC28A015FEAEE495D;BDUSS=WxPaWE5S0xQNVBNbmJHNTVia2tldUtPd2cxVTBpUmJwczhsc0ZzY3QzMW8yd2huRVFBQUFBJCQAAAAAAAAAAAEAAACuhdCQMTIzxOPU2jEyMTM4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGhO4WZoTuFmS;csrfToken=XXCrMLGWJdcYW8LtjmCYTtHx;H_PS_PSSID=60274_60729_60360_60732_60797;H_WISE_SIDS=110085_613052_619433_621090_621364_621324_621649_621756_621758_621821;H_WISE_SIDS_BFESS=110085_613052_619433_621090_621364_621324_621649_621756_621758_621821;Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0=1726159132;PANPSC=3865015075917826769%3ACU2JWesajwByPfGOomAcr8Wn1hbHg1WZbtDq%2BK%2BOodwOYC6rNtBREiQxbl68m9lcBm6rqQ5QdYIKCzV4mddQKizirhbJpOZBwhRIQmAoMSKHkrigi2TxuAjHRUw%2FZR6kLvxjdeGWe15rqCNYc2LuOFCHZGOaQdgCY8uG8AM%2BY0Ih6uZoP3DwQ7BnXFvU9LYk9FYxwFKTFsLUPkQIWbHzQjCo8bcT1HMK;PSTM=1725626969;RT="z=1&dm=baidu.com&si=ac5d35eb-2779-4470-a545-1729edf4d975&ss=m0z2y3r8&sl=0&tt=0&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=pnzl&ul=uj8o&hd=uj93";SCRC=5260bd92bbce925b9e754cd35332e6de;XFCS=E0A4B97B8C491E9BD94F2B7E0B800D7E116FEB5CA426D5BDE111D8BBE66B5175;XFT=Vfmu3rMfuT/WzZImM6cNQk5tWt/n6Ant7+dCz5HZsck="""
    )
    pprint(bd.list_all("/"))
    pprint(bd.create_dir("/我的资源"))
    pprint(
        bd.auto_save(
            "https://pan.baidu.com/s/1gtgxD8FlQ26JEGjmBORnfg?pwd=m9vd", "/auto_get"
        )
    )
    search_res = bd.search_all("你好")
    pprint(search_res.__len__())
    pprint(search_res[:5])
