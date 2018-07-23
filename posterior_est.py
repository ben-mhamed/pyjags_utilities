def posterior_est(samples):
    nvars = len(samples)
    labels = list(samples.keys())
    n = 0
    for i in range(len(samples)):
        n+=samples[labels[i]].shape[0]
    smry = pd.DataFrame(columns=['Mean','SD','2.5%','25%','50%','75%','97.5%'],index=range(n))
    varnames = list()
    k = 0
    for i in range(nvars):
        m=samples[labels[i]].shape[0]
        if m==1:
            smry['Mean'].values[k] = np.mean(samples[labels[i]])
            smry['SD'].values[k] = np.std(samples[labels[i]])
            smry['2.5%'].values[k] = np.percentile(samples[labels[i]],2.5)
            smry['25%'].values[k] = np.percentile(samples[labels[i]],25)
            smry['50%'].values[k] = np.median(samples[labels[i]])
            smry['75%'].values[k] = np.percentile(samples[labels[i]],75)
            smry['97.5%'].values[k] = np.percentile(samples[labels[i]],97.5)
            varnames.append(labels[i])
            k+=1
        else:
            for j in range(m):
                smry['Mean'].values[k] = np.mean(samples[labels[i]][j])
                smry['SD'].values[k] = np.std(samples[labels[i]][j])
                smry['2.5%'].values[k] = np.percentile(samples[labels[i]][j],2.5)
                smry['25%'].values[k] = np.percentile(samples[labels[i]][j],25)
                smry['50%'].values[k] = np.median(samples[labels[i]][j])
                smry['75%'].values[k] = np.percentile(samples[labels[i]][j],75)
                smry['97.5%'].values[k] = np.percentile(samples[labels[i]][j],97.5)
                z = labels[i] + "[{}]".format(j)
                varnames.append(z)
                k+=1
    smry.index = varnames
    return smry
