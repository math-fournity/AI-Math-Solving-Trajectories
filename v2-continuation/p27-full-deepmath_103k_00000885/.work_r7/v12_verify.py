import numpy as np, sympy as sp, mpmath as mp
from scipy.integrate import quad
from scipy.special import gamma as G
from numpy.polynomial.legendre import leggauss
mp.mp.dps=15

print("="*72); print("V1a-sympy: 有理 beta 常数公式核对")
for bb in [sp.Rational(1,2), sp.Rational(3,2)]:
    tgt = sp.simplify(sp.pi/(2*sp.gamma(bb+1)*sp.sin(sp.pi*bb/2)))
    f = lambda uu: (1-mp.cos(uu))/uu**(1+bb)
    Inum = mp.quad(f,[0,1]) + mp.quadosc(f,[1,mp.inf],omega=1)
    print(f"beta={bb}: 公式值={float(tgt):.10f} ; mpmath={float(Inum):.10f} ; 差={float(abs(Inum-tgt)):.2e}")

print("-"*72)
print("V1b: 高斯加权恒等式定出 c_beta")
def gauss_check(beta, sigma):
    lhs = sigma**beta * 2**(beta/2) * G((1+beta)/2)/np.sqrt(np.pi)
    f = lambda xi: (1-np.exp(-xi*xi*sigma*sigma/2))/abs(xi)**(1+beta)
    I = 2*(quad(f,0,1,limit=200)[0] + quad(f,1,np.inf,limit=400)[0])
    c = G(beta+1)*np.sin(np.pi*beta/2)/np.pi
    return abs(lhs - c*I)/lhs
mx=max(gauss_check(b,s) for b in [0.3,0.5,0.7,1.0,1.3,1.7] for s in [0.4,1.0,2.0])
print("max rel err over β∈{0.3..1.7},σ∈{0.4,1,2}:", f"{mx:.2e}")

print("-"*72)
print("V1c: mp.quadosc 直接验证 |x|^b == c_b∫R(1-cos ξx)|ξ|^-1-b")
def full(beta,x):
    f=lambda xi:(1-mp.cos(xi*x))/(abs(xi)**(1+beta)) if xi else mp.mpf(0)
    return 2*(mp.quad(f,[0,1]) + mp.quadosc(f,[1,mp.inf],omega=float(x)))
for beta,x in [(mp.mpf('0.7'),mp.mpf('1.3')), (mp.mpf('1.7'),mp.mpf('0.5'))]:
    c=mp.gamma(beta+1)*mp.sin(mp.pi*beta/2)/mp.pi
    lhs,rhs=abs(x)**beta, c*full(beta,x)
    print(f"β={beta},x={x}: {float(lhs):.10f} vs {float(rhs):.10f} relerr={float(abs(lhs-rhs)/lhs):.1e}")

print("="*72)
print("V2: Fubini 恒等式 E==∫gV + Step3 三角代数")
n=120; t,w = leggauss(n); t=(t+1)/2; w=w/2
rng=np.random.default_rng(7)
W2 = w[:,None]*w[None,:]
for trial in range(3):
    coef = rng.normal(size=6)
    gv = np.polyval(coef[::-1], t)
    A = w@gv; GG = gv[:,None]*gv[None,:]
    for beta in [0.4,0.9,1.0,1.6]:
        K = np.abs(t[:,None]-t[None,:])**beta
        E_double = float((W2*GG*K).sum())
        V = K @ (w*gv)
        E_pot = float(w @ (gv*V))
        errs=[]
        for xi in [0.7,2.3,5.1]:
            gh_re, gh_im = w@(gv*np.cos(xi*t)), w@(gv*np.sin(xi*t))
            Phi = float((W2*GG*(1-np.cos(xi*(t[:,None]-t[None,:])))).sum())
            errs.append(abs(A*A-(gh_re**2+gh_im**2)-Phi))
        print(f"trial{trial} β={beta:.1f}: |E_double-E_pot|={abs(E_double-E_pot):.2e}   maxerr(A²-|ĝ|²==Φ)={max(errs):.2e}")
