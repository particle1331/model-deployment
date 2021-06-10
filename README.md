# Deployment of Machine Learning Models
*Learn how to put your machine learning models live and start getting true value from your machine learning models.*


<br>

- [Deployment of Machine Learning Models](#deployment-of-machine-learning-models)
  - [Course objectives](#course-objectives)
  - [What is model deployment?](#what-is-model-deployment)
  - [Topics covered](#topics-covered)
  - [Quick links](#quick-links)

<br>


**Reference**: [Deployment of Machine Learning Models](https://www.udemy.com/course/deployment-of-machine-learning-models) by Soledad Galli & Christopher Samiullah @ Udemy.

<br>

## Course objectives

---

After this course you should

1. Be able to take machine learning models from research stage to a fully integrated API.
2. Be familiar with various coding best practices.
3. Feel comfortable to deploy any machine learning model in various infrastructures.


<br>

## What is model deployment?

---


<br>

<p align='center'>
    <img src="images/model_deployment.png"
        width=600 />
    <br>
    <b>Figure. </b> ML models in production.
    </p>
<br>

- No machine learning model brings true value until it is fully integrated and can be used to score real data. So model deployment is the most important and yet most difficult part of any typical machine learning pipeline. Modern deployment presents the challenges of traditional software like reliability, reusability, maintainability and flexibility, and it also presents additional challenges that are specific to machine learning, like **reproducibility**.
  
- Model deployment requires coordination between data scientists, I.T. teams and their ops software developers, and business professionals to make sure the model works reliably in their organization's production environment.

- There is often a discrepancy between the programming language in which the machine learning model is written and the languages your production system can understand and recoding the model can extend the project timeline by weeks or months and also risks lack of reproducibility. 
  
- To maximize the value of the machine learning model we create, we need to be able to reliably extract the predictions from the model and share them with other systems. The course will discuss the best practices and available solutions to mitigate the challenges that deployment of machine learning models present and streamline the integration of our machine learning models into production.

<br>

**Remark.** A more complete description is that we deploy **pipelines** not just models. This includes data preprocessing pipeline, feature engineering and selection pipeline, as well as prediction serving pipeline, monitoring and evaluation pipeline, and so on. Thus, our goal is to build **reproducible machine learning pipelines.** Tests for ML systems should always include reproducibility along with tests of performance and functionality. 

<br>

## Topics covered

---
<br>

- Entire ML life cycle
- Research phase
- Transform research code into production code + best practices
- Create an API and make API calls
- Testing to make sure production models corroborate research models given same data
- Continuous Integration (CI)
- Various deployment solutions, e.g. PaaS, IaaS
- Docker for reproducibility and robustness

<br>

<p align='center'>
    <img src="images/ml_deployment_pipeline.png"
        width=600 />
    <br>
    <b>Figure. </b> Course sections dealing with the phases of model deployment. 
    </p>
<br>

<br>

## Quick links

---


<br>

**Blogs / Talks / Tutorials**

- [The Machine Learning Reproducibility Crisis](https://petewarden.com/2018/03/19/the-machine-learning-reproducibility-crisis/)
- [Reproducible Machine Learning](http://www.rctatman.com/files/Tatman_2018_ReproducibleML.pdf)
- [Introducing FBLearner Flow: Facebook’s AI backbone](https://engineering.fb.com/2016/05/09/core-data/introducing-fblearner-flow-facebook-s-ai-backbone/)
- [System Architectures for Personalization and Recommendation](https://netflixtechblog.com/system-architectures-for-personalization-and-recommendation-e081aa94b5d8)
- [Meet Michelangelo: Uber’s Machine Learning Platform](https://eng.uber.com/michelangelo-machine-learning-platform/)
- [DSF Mainstage Day 2019 - Building and Deploying Reproducible ML Pipelines](https://www.youtube.com/watch?v=7jKTofl2vmM&ab_channel=DataScienceFestival)
- [YAML Tutorial | Using YAML With Python | PyYAML](https://dev.to/developertharun/yaml-tutorial-using-yaml-with-python-pyyaml-443d)
- [Soledad Galli - Machine Learning in Financial Credit Risk Assessment](https://www.youtube.com/watch?v=KHGGlozsRtA&ab_channel=PyData)
- [Jake Vanderplas. Performance Python: Seven Strategies for Optimizing Your Numerical Code](https://speakerdeck.com/pycon2018/jake-vanderplas-performance-python-seven-strategies-for-optimizing-your-numerical-code)
- [Python Type Checking](https://realpython.com/python-type-checking/)
- [Type Checked Python in the Real World](https://speakerdeck.com/pycon2018/carl-meyer-type-checked-python-in-the-real-world)

<br>

**Papers**

- [KDD Cup 2009. Knowledge Discovery. Challenges in Machine Learning, Volume 3](http://www.mtome.com/Publications/CiML/CiML-v3-book.pdf)
- [Sugimura & Hartl. Building a Reproducible Machine Learning Pipeline](https://arxiv.org/ftp/arxiv/papers/1810/1810.04570.pdf)
- [Li Erran et. al. Scaling Machine Learning as a Service](http://proceedings.mlr.press/v67/li17a/li17a.pdf)
- [Ghanta et. al. A Systems Perspective to Reproducibility in Production Machine Learning Domain](https://openreview.net/pdf?id=Byl4vavigX)
- [Hidden Technical Debt in Machine Learning Systems](https://papers.nips.cc/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf)
- [TFX: A TensorFlow-Based Production-Scale Machine Learning Platform](https://research.google/pubs/pub46484/)
- [What’s your ML Test Score? A rubric for ML production systems](https://storage.googleapis.com/pub-tools-public-publication-data/pdf/45742.pdf)

<br>
