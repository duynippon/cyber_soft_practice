class Hoc_vien:
    def __init__(self, maHV: int, tenHV: str, ngaySinh: int, khoaHoc: list[str] = None):
        self.maHV = maHV
        self.tenHV = tenHV
        self.ngaySinh = ngaySinh

    def dang_ky(self, khoaHoc: list[str]):
        self.khoaHoc = khoaHoc

    def hien_thi(self):
        return self.khoaHoc


class khoahoc:
    """
    1 = hoc online
    2 = hoc offline
    """

    def __init__(self, makhoahoc: int, tenKhoahoc: str, hinhthuc: bool, hocphi: int):
        self.makhoahoc = makhoahoc
        self.tenKhoahoc = tenKhoahoc
        self.hinhthuc = hinhthuc
        self.hocphi = hocphi

    def hienthikhoahoc(self):
        result = f"Ma khoa hoc: {self.makhoahoc}\nTen khoa hoc: {self.tenKhoahoc}\nHinh thuc: {self.hinhthuc}\nHoc phi: {self.hocphi}"
        return result
