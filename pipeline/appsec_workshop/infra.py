from aws_cdk import (
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_ecs_patterns as ecs_patterns,
    core
)

class Infra(core.Construct):

    @property
    def staging_vpc(self):
        return self._staging_vpc
    
    @property
    def staging_cluster(self):
        return self._staging_cluster

    def __init__(self, scope: core.Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        # Staging VPC
        self._staging_vpc = ec2.Vpc(
            self, "StagingVPC",
            max_azs=2
        )
        
        # Staging Cluster
        self._staging_cluster = ecs.Cluster(
            self, "StagingCluster",
            vpc=self._staging_vpc
        )

        # Production VPC
        # self._production_vpc = ec2.Vpc(
        #     self, "ProductionVPC",
        #     max_azs=2
        # )

        # # Production Cluster
        # self._production_cluster = ecs.Cluster(
        #     self, "ProductionCluster",
        #     vpc=self._production_vpc
        # )


        