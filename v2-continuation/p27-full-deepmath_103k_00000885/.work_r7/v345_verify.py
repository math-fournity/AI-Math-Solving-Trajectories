import numpy as np
from numpy.polynomial.legendre import leggauss, Legendre
from scipy.integrate import quad

def R_H(s,t,H):
    return 0.5*(np.abs(s)**(2*H)+np.abs(t)**(2*H)-np.abs(s-t)**(2*H))

print("="*72)
print("V5: RKHS Gram 矩阵 PSD 验证  min_eig(G)>=0")
n=64; t,w = leggauss(n); t=(t+1)/2; w=w/2
for H in [0.1,0.25,0.4,0.5,0.6,0.75,0.9,0.99]:
    Gm = R_H(t[:,None],t[None,:],H)
    ev = np.linalg.eigvalsh((Gm+Gm.T)/2)
    print(f"H={H:4.2f}: min_eig={ev.min():.3e}  (n={n})")

print("="*72)
print("V3: 算子 g -> U_g mod 常数 在多项式子空间(d<=8)的最小奇异值")
d=8; deg=np.arange(1,d+1)
Phi = np.array([np.polynomial.legendre.legval(t, np.eye(20)[k]) for k in deg]).T  # P1..P8 在节点
# GL 内积正交归一化
Gm_phi = Phi.T @ (Phi*w[:,None])
ev,Q = np.linalg.eigh(Gm_phi)
Phi_o = Phi @ (Q/np.sqrt(ev))
for H in [0.15,0.3,0.5,0.7,0.85,0.95]:
    T = R_H(t[:,None],t[None,:],H)*w[None,:]     # T[i,j]=w_j R_H(t_j,u_i)
    Bm = T - T.mean(axis=0,keepdims=True)        # 商掉常数 (目标空间)
    M = Bm @ Phi_o
    sv = np.linalg.svd(M,compute_uv=False)
    print(f"H={H:4.2f}: sigma_max={sv[0]:.3e} sigma_min={sv[-1]:.3e} cond={sv[0]/sv[-1]:.2e}")

print("-"*72)
print("V3b: 直接证伪尝试——非零 g 的 U_g 离 'Au^β+D' 有多远 (相对残差)")
u_fine = np.linspace(0,1,401)
for H in [0.3,0.5,0.7]:
    for name,gf in [("sin(pi t)",lambda x:np.sin(np.pi*x)),
                    ("P2(t)",lambda x:(3*x**2-1)/2),
                    ("t^2",lambda x:x**2)]:
        U = np.array([quad(lambda tt: gf(tt)*R_H(tt,uu,H),0,1,limit=200)[0] for uu in u_fine])
        # 最小二乘拟合 A u^β + D
        beta=2*H
        Mfit = np.stack([u_fine**beta, np.ones_like(u_fine)],axis=1)
        coef,res,rk,sv_ = np.linalg.lstsq(Mfit,U,rcond=None)
        rel = np.linalg.norm(U-Mfit@coef)/np.linalg.norm(U)
        print(f"H={H}: g={name:10s} 相对拟合残差={rel:.3e}  (若 Lemma A 错则应为 ~0)")

print("="*72)
print("V4: 微分引理公式对随机多项式 g 验证 (V' 与 V'')")
rng=np.random.default_rng(3)
def V_of(gf,s,beta):
    return quad(lambda tt: abs(s-tt)**beta*gf(tt),0,1,limit=300)[0]
def dV_formula(gf,s,beta):
    p1=quad(lambda tt:(s-tt)**(beta-1)*gf(tt),0,s,limit=300)[0]
    p2=quad(lambda tt:(tt-s)**(beta-1)*gf(tt),s,1,limit=300)[0]
    return beta*(p1-p2)
def ddV_formula(gf,s,beta):
    p1=quad(lambda tt:(s-tt)**(beta-2)*gf(tt),0,s,limit=300)[0]
    p2=quad(lambda tt:(tt-s)**(beta-2)*gf(tt),s,1,limit=300)[0]
    return beta*(beta-1)*(p1+p2)
coef = rng.normal(size=4)
gf = np.polynomial.polynomial.Polynomial(coef)
for beta in [0.35,0.7,1.0,1.5,1.85]:
    line=f"β={beta:4.2f}: "
    for s0 in [0.25,0.5,0.8]:
        h=1e-4
        fd=(V_of(gf,s0+h,beta)-V_of(gf,s0-h,beta))/(2*h)
        an=dV_formula(gf,s0,beta)
        line+=f"|V'-formula|({s0})={abs(fd-an)/max(1,abs(an)):.1e}  "
    if beta>1:
        for s0 in [0.3,0.6]:
            h=1e-3
            fdd=(V_of(gf,s0+h,beta)-2*V_of(gf,s0,beta)+V_of(gf,s0-h,beta))/h**2
            andd=ddV_formula(gf,s0,beta)
            line+=f"|V''-f|({s0})={abs(fdd-andd)/max(1,abs(andd)):.1e}  "
    print(line)

print("-"*72)
print("V4b: Step1 三分支机制演示 (g 随机多项式, A≠0)")
A = float(np.polynomial.polynomial.Polynomial(coef).integ()(1))
print(f"选取的 g: A=∫g={A:.4f} (非零)")
for beta in [0.35,0.7]:
    exp=beta-1
    for u0 in [1e-2,1e-3]:
        F=quad(lambda tt:(u0-tt)**exp*float(gf(tt)),0,u0,limit=500)[0]-quad(lambda tt:(tt-u0)**exp*float(gf(tt)),u0,1,limit=500)[0]
        scaled=F*u0**(-exp)
        print(f"β={beta}: u={u0:.0e}  F(u)={F:+.4e}  F(u)/u^(β-1)={scaled:+.4e}")
