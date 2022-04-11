import hudson.plugins.git.GitSCM;
import hudson.plugins.git.BranchSpec;
import hudson.model.FreeStyleProject;
import hudson.tasks.Shell;

import jenkins.model.Jenkins;
import org.jenkinsci.plugins.workflow.cps.CpsFlowDefinition;
import org.jenkinsci.plugins.workflow.job.WorkflowJob;


jenkins = Jenkins.instance;

scm = new GitSCM("https://github.com/gwynforthewyn/jinkies");
scm.branches = [new BranchSpec("*/main")];

workflowJob = new WorkflowJob(jenkins, "jinkies-up-in-this-bitch");

jenkinsFileLocation = System.getenv('JINKIES_SEED_JENKINSFILE')

jobDefinition = new File(jenkinsFileLocation).getText('UTF-8')

workflowJob.definition = new CpsFlowDefinition(jobDefinition, true);
jenkins.add(workflowJob, workflowJob.name);
