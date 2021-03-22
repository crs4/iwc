import pathlib
from rocrate.rocrate import ROCrate

THIS_DIR = pathlib.Path(__file__).absolute().parent
CRATE_DIR = THIS_DIR / "travis-example"
WORKFLOW_ID = "https://raw.githubusercontent.com/galaxyproject/iwc/d796d175a7f3b531898a229090c6540f0409b075/workflows/sars-cov-2-variant-calling/sars-cov-2-pe-illumina-artic-variant-calling/pe-artic-variation.ga"
TRAVIS_URL = "https://travis-ci.org"
TRAVIS_RESOURCE = "github/crs4/iwc/builds"


def main():
    crate = ROCrate(CRATE_DIR, init=True, load_preview=True)
    workflow = crate.add_workflow(WORKFLOW_ID, main=True, lang="galaxy",
                                  gen_cwl=False)
    workflow["name"] = WORKFLOW_ID.rsplit("/", 1)[-1]
    crate.root_dataset["author"] = "Wolfgang Maier"
    crate.root_dataset["isBasedOn"] = "https://github.com/iwc-workflows/sars-cov-2-pe-illumina-artic-variant-calling"
    crate.root_dataset["license"] = "MIT"
    suite = crate.add_test_suite(identifier="#test1")
    crate.add_test_instance(suite, TRAVIS_URL, resource=TRAVIS_RESOURCE,
                            service="travis", identifier="test1_1")
    crate.metadata.write(CRATE_DIR)


if __name__ == "__main__":
    main()
