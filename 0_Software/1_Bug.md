

### 01 Can't locate Bio/Perl.pm in @INC (you may need to install the Bio::Perl module)

The original error is :
`Can't locate Bio/Perl.pm in @INC (you may need to install the Bio::Perl module) (@INC contains: /scratch/work/chengg1/myconda/conda_envs/bioperl/lib/perl5/5.32/site_perl /scratch/work/chengg1/myconda/conda_envs/bioperl/lib/perl5/site_perl /scratch/work/chengg1/myconda/conda_envs/bioperl/lib/perl5/5.32/vendor_perl /scratch/work/chengg1/myconda/conda_envs/bioperl/lib/perl5/vendor_perl /scratch/work/chengg1/myconda/conda_envs/bioperl/lib/perl5/5.32/core_perl /scratch/work/chengg1/myconda/conda_envs/bioperl/lib/perl5/core_perl .) `

This is caused by the version. The `perl` version and the `Bio`(or `Seq.pm`) should be the same.

- `perl -v`
- This is perl 5, version 22, subversion 0 (v5.22.0) built for x86_64-linux-thread-multi

- `find /scratch/work/chengg1/myconda/conda_envs/mybioperl -iname 'Seq.pm'`
- /scratch/work/chengg1/myconda/conda_envs/mybioperl/lib/perl5/site_perl/5.22.0/Bio/Seq.pm

- `find /scratch/work/chengg1/myconda/conda_envs/mybioperl -iname 'Bio'`
- /scratch/work/chengg1/myconda/conda_envs/mybioperl/lib/perl5/site_perl/5.22.0/x86_64-linux-thread-multi/auto/Bio
- /scratch/work/chengg1/myconda/conda_envs/mybioperl/lib/perl5/site_perl/5.22.0/Bio

In this case, the version are the same: `5.22.0`

Reference: https://github.com/tseemann/snippy/issues/469
