import numpy as np
rng=np.random.default_rng(11)
print("V6: fBm Monte Carlo 定性检查 Z=∫B⁴ 的经验分布 (Cholesky 模拟)")
n=256; t=(np.arange(1,n+1))/n
for H in [0.3,0.5,0.7]:
    C=0.5*(np.abs(t[:,None])**(2*H)+np.abs(t[None,:])**(2*H)-np.abs(t[:,None]-t[None,:])**(2*H))
    L=np.linalg.cholesky(C+1e-14*np.eye(n))
    NPATH=20000
    Zs=[]
    for _ in range(NPATH//1000):
        B=L@rng.standard_normal((n,1000))
        Z=(B**4).mean(axis=0)          # ∫₀¹B⁴dt 的 Riemann 近似
        Zs.append(Z)
    Z=np.concatenate(Zs)
    qs=np.quantile(Z,[0.01,0.25,0.5,0.75,0.99])
    hist,_=np.histogram(Z,bins=60,density=True)
    # 平滑度指标: 直方图相邻 bin 密度差的相对波动 (有密度的分布应无空档/尖刺)
    gaps=(hist[:-1]==0)&(hist[1:]>0)
    print(f"H={H}: mean={Z.mean():.4f}(理论E[B_t⁴]均值≈{np.mean(3*(t**(2*H))):.4f}) "
          f"分位数={np.round(qs,3)} 非零bin占比={(hist>0).mean():.3f} 相邻空档数={int(gaps.sum())}")
