# Llama cloud
##  LlamaCloudIndex [#](https://developers.llamaindex.ai/python/framework-api-reference/indices/llama_cloud/#llama_index.indices.managed.llama_cloud.LlamaCloudIndex "Permanent link")
Bases: `BaseManagedIndex`
A managed index that stores documents in LlamaCloud.
There are two main ways to use this index:
  1. Connect to an existing LlamaCloud index: 
```
# Connect using index ID (same as pipeline ID)
index = LlamaCloudIndex(id="<index_id>")

# Or connect using index name
index = LlamaCloudIndex(
    name="my_index",
    project_name="my_project",
    organization_id="my_org_id"
)

```

  2. Create a new index with documents: 
```
documents = [Document(...), Document(...)]
index = LlamaCloudIndex.from_documents(
    documents,
    name="my_new_index",
    project_name="my_project",
    organization_id="my_org_id"
)

```



The index supports standard operations like retrieval and querying through the as_query_engine() and as_retriever() methods.
Source code in `llama_index/indices/managed/llama_cloud/base.py`
```
  64
  65
  66
  67
  68
  69
  70
  71
  72
  73
  74
  75
  76
  77
  78
  79
  80
  81
  82
  83
  84
  85
  86
  87
  88
  89
  90
  91
  92
  93
  94
  95
  96
  97
  98
  99
 100
 101
 102
 103
 104
 105
 106
 107
 108
 109
 110
 111
 112
 113
 114
 115
 116
 117
 118
 119
 120
 121
 122
 123
 124
 125
 126
 127
 128
 129
 130
 131
 132
 133
 134
 135
 136
 137
 138
 139
 140
 141
 142
 143
 144
 145
 146
 147
 148
 149
 150
 151
 152
 153
 154
 155
 156
 157
 158
 159
 160
 161
 162
 163
 164
 165
 166
 167
 168
 169
 170
 171
 172
 173
 174
 175
 176
 177
 178
 179
 180
 181
 182
 183
 184
 185
 186
 187
 188
 189
 190
 191
 192
 193
 194
 195
 196
 197
 198
 199
 200
 201
 202
 203
 204
 205
 206
 207
 208
 209
 210
 211
 212
 213
 214
 215
 216
 217
 218
 219
 220
 221
 222
 223
 224
 225
 226
 227
 228
 229
 230
 231
 232
 233
 234
 235
 236
 237
 238
 239
 240
 241
 242
 243
 244
 245
 246
 247
 248
 249
 250
 251
 252
 253
 254
 255
 256
 257
 258
 259
 260
 261
 262
 263
 264
 265
 266
 267
 268
 269
 270
 271
 272
 273
 274
 275
 276
 277
 278
 279
 280
 281
 282
 283
 284
 285
 286
 287
 288
 289
 290
 291
 292
 293
 294
 295
 296
 297
 298
 299
 300
 301
 302
 303
 304
 305
 306
 307
 308
 309
 310
 311
 312
 313
 314
 315
 316
 317
 318
 319
 320
 321
 322
 323
 324
 325
 326
 327
 328
 329
 330
 331
 332
 333
 334
 335
 336
 337
 338
 339
 340
 341
 342
 343
 344
 345
 346
 347
 348
 349
 350
 351
 352
 353
 354
 355
 356
 357
 358
 359
 360
 361
 362
 363
 364
 365
 366
 367
 368
 369
 370
 371
 372
 373
 374
 375
 376
 377
 378
 379
 380
 381
 382
 383
 384
 385
 386
 387
 388
 389
 390
 391
 392
 393
 394
 395
 396
 397
 398
 399
 400
 401
 402
 403
 404
 405
 406
 407
 408
 409
 410
 411
 412
 413
 414
 415
 416
 417
 418
 419
 420
 421
 422
 423
 424
 425
 426
 427
 428
 429
 430
 431
 432
 433
 434
 435
 436
 437
 438
 439
 440
 441
 442
 443
 444
 445
 446
 447
 448
 449
 450
 451
 452
 453
 454
 455
 456
 457
 458
 459
 460
 461
 462
 463
 464
 465
 466
 467
 468
 469
 470
 471
 472
 473
 474
 475
 476
 477
 478
 479
 480
 481
 482
 483
 484
 485
 486
 487
 488
 489
 490
 491
 492
 493
 494
 495
 496
 497
 498
 499
 500
 501
 502
 503
 504
 505
 506
 507
 508
 509
 510
 511
 512
 513
 514
 515
 516
 517
 518
 519
 520
 521
 522
 523
 524
 525
 526
 527
 528
 529
 530
 531
 532
 533
 534
 535
 536
 537
 538
 539
 540
 541
 542
 543
 544
 545
 546
 547
 548
 549
 550
 551
 552
 553
 554
 555
 556
 557
 558
 559
 560
 561
 562
 563
 564
 565
 566
 567
 568
 569
 570
 571
 572
 573
 574
 575
 576
 577
 578
 579
 580
 581
 582
 583
 584
 585
 586
 587
 588
 589
 590
 591
 592
 593
 594
 595
 596
 597
 598
 599
 600
 601
 602
 603
 604
 605
 606
 607
 608
 609
 610
 611
 612
 613
 614
 615
 616
 617
 618
 619
 620
 621
 622
 623
 624
 625
 626
 627
 628
 629
 630
 631
 632
 633
 634
 635
 636
 637
 638
 639
 640
 641
 642
 643
 644
 645
 646
 647
 648
 649
 650
 651
 652
 653
 654
 655
 656
 657
 658
 659
 660
 661
 662
 663
 664
 665
 666
 667
 668
 669
 670
 671
 672
 673
 674
 675
 676
 677
 678
 679
 680
 681
 682
 683
 684
 685
 686
 687
 688
 689
 690
 691
 692
 693
 694
 695
 696
 697
 698
 699
 700
 701
 702
 703
 704
 705
 706
 707
 708
 709
 710
 711
 712
 713
 714
 715
 716
 717
 718
 719
 720
 721
 722
 723
 724
 725
 726
 727
 728
 729
 730
 731
 732
 733
 734
 735
 736
 737
 738
 739
 740
 741
 742
 743
 744
 745
 746
 747
 748
 749
 750
 751
 752
 753
 754
 755
 756
 757
 758
 759
 760
 761
 762
 763
 764
 765
 766
 767
 768
 769
 770
 771
 772
 773
 774
 775
 776
 777
 778
 779
 780
 781
 782
 783
 784
 785
 786
 787
 788
 789
 790
 791
 792
 793
 794
 795
 796
 797
 798
 799
 800
 801
 802
 803
 804
 805
 806
 807
 808
 809
 810
 811
 812
 813
 814
 815
 816
 817
 818
 819
 820
 821
 822
 823
 824
 825
 826
 827
 828
 829
 830
 831
 832
 833
 834
 835
 836
 837
 838
 839
 840
 841
 842
 843
 844
 845
 846
 847
 848
 849
 850
 851
 852
 853
 854
 855
 856
 857
 858
 859
 860
 861
 862
 863
 864
 865
 866
 867
 868
 869
 870
 871
 872
 873
 874
 875
 876
 877
 878
 879
 880
 881
 882
 883
 884
 885
 886
 887
 888
 889
 890
 891
 892
 893
 894
 895
 896
 897
 898
 899
 900
 901
 902
 903
 904
 905
 906
 907
 908
 909
 910
 911
 912
 913
 914
 915
 916
 917
 918
 919
 920
 921
 922
 923
 924
 925
 926
 927
 928
 929
 930
 931
 932
 933
 934
 935
 936
 937
 938
 939
 940
 941
 942
 943
 944
 945
 946
 947
 948
 949
 950
 951
 952
 953
 954
 955
 956
 957
 958
 959
 960
 961
 962
 963
 964
 965
 966
 967
 968
 969
 970
 971
 972
 973
 974
 975
 976
 977
 978
 979
 980
 981
 982
 983
 984
 985
 986
 987
 988
 989
 990
 991
 992
 993
 994
 995
 996
 997
 998
 999
1000
1001
1002
1003
1004
1005
1006
1007
1008
1009
1010
1011
1012
1013
1014
1015
1016
1017
1018
1019
1020
1021
1022
1023
1024
1025
1026
1027
1028
1029
1030
1031
1032
1033
1034
1035
1036
1037
1038
1039
1040
1041
1042
1043
1044
1045
1046
1047
1048
1049
1050
1051
1052
1053
1054
1055
1056
1057
1058
1059
1060
1061
1062
1063
1064
1065
1066
1067
1068
1069
1070
```
| ```
@deprecated(
    reason=DEPRECATION_REASON,
    version="0.9.1",
    action="once",
)
class LlamaCloudIndex(BaseManagedIndex):
"""
    A managed index that stores documents in LlamaCloud.

    There are two main ways to use this index:

    1. Connect to an existing LlamaCloud index:
        ```python
        # Connect using index ID (same as pipeline ID)
        index = LlamaCloudIndex(id="<index_id>")

        # Or connect using index name
        index = LlamaCloudIndex(
            name="my_index",
            project_name="my_project",
            organization_id="my_org_id"

        ```

    2. Create a new index with documents:
        ```python
        documents = [Document(...), Document(...)]
        index = LlamaCloudIndex.from_documents(
            documents,
            name="my_new_index",
            project_name="my_project",
            organization_id="my_org_id"

        ```

    The index supports standard operations like retrieval and querying
    through the as_query_engine() and as_retriever() methods.
    """

    def __init__(
        self,
        # index identifier
        name: Optional[str] = None,
        pipeline_id: Optional[str] = None,
        index_id: Optional[str] = None,  # alias for pipeline_id
        id: Optional[str] = None,  # alias for pipeline_id
        # project identifier
        project_id: Optional[str] = None,
        project_name: str = DEFAULT_PROJECT_NAME,
        organization_id: Optional[str] = None,
        # connection params
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        app_url: Optional[str] = None,
        timeout: int = 60,
        httpx_client: Optional[httpx.Client] = None,
        async_httpx_client: Optional[httpx.AsyncClient] = None,
        # misc
        show_progress: bool = False,
        callback_manager: Optional[CallbackManager] = None,
        # deprecated
        nodes: Optional[List[BaseNode]] = None,
        transformations: Optional[List[TransformComponent]] = None,
        **kwargs: Any,
    ) -> None:
"""Initialize the Platform Index."""
        if sum([bool(id), bool(index_id), bool(pipeline_id), bool(name)]) != 1:
            raise ValueError(
                "Exactly one of `name`, `id`, `pipeline_id` or `index_id` must be provided to identify the index."
            )

        if nodes is not None:
            # TODO: How to handle uploading nodes without running transforms on them?
            raise ValueError("LlamaCloudIndex does not support nodes on initialization")

        if transformations is not None:
            raise ValueError(
                "Setting transformations is deprecated for LlamaCloudIndex, please use the `transform_config` and `embedding_config` parameters instead."
            )

        # initialize clients
        self._httpx_client = httpx_client
        self._async_httpx_client = async_httpx_client
        self._client = get_client(
            api_key=api_key,
            base_url=base_url,
            app_url=app_url,
            timeout=timeout,
            httpx_client=httpx_client,
        )
        self._aclient = get_aclient(
            api_key=api_key,
            base_url=base_url,
            app_url=app_url,
            timeout=timeout,
            httpx_client=async_httpx_client,
        )

        self.organization_id = organization_id
        pipeline_id = id or index_id or pipeline_id

        self.project, self.pipeline = resolve_project_and_pipeline(
            self._client, name, pipeline_id, project_name, project_id, organization_id
        )
        self.name = self.pipeline.name
        self.project_name = self.project.name

        self._api_key = api_key
        self._base_url = base_url
        self._app_url = app_url
        self._timeout = timeout
        self._show_progress = show_progress
        self._callback_manager = callback_manager or Settings.callback_manager

    @property
    def id(self) -> str:
"""Return the pipeline (aka index) ID."""
        return self.pipeline.id

    def _wait_for_resources(
        self,
        resource_ids: Sequence[str],
        get_status_fn: Callable[[str], ManagedIngestionStatusResponse],
        resource_name: str,
        verbose: bool,
        raise_on_error: bool,
        sleep_interval: float,
    ) -> None:
"""
        Poll `get_status_fn` until every id in `resource_ids` is finished.

        Args:
            resource_ids: Iterable of resource ids to watch.
            get_status_fn: Callable that maps a resource id → ManagedIngestionStatus.
            resource_name: Text used in log / error messages: "file", "document", ….
            verbose: Print a progress bar.
            raise_on_error: Whether to raise on ManagedIngestionStatus.ERROR.
            sleep_interval: Seconds between polls (min 0.5 s to avoid rate-limits).

        """
        if not resource_ids:  # nothing to do
            return

        if verbose:
            print(
                f"Loading {resource_name}{'s'iflen(resource_ids)1else''}",
            )

        pending: set[str] = set(resource_ids)
        while pending:
            finished: set[str] = set()
            for rid in pending:
                try:
                    status_response = get_status_fn(rid)
                    status = status_response.status
                    if status in (
                        ManagedIngestionStatus.NOT_STARTED,
                        ManagedIngestionStatus.IN_PROGRESS,
                    ):
                        continue  # still working

                    if status == ManagedIngestionStatus.ERROR:
                        if verbose:
                            print(
                                f"{resource_name.capitalize()} ingestion failed for {rid}"
                            )
                        if raise_on_error:
                            raise ValueError(
                                f"{resource_name.capitalize()} ingestion failed for {rid}"
                            )

                    finished.add(rid)
                    if verbose:
                        print(
                            f"{resource_name.capitalize()} ingestion finished for {rid}"
                        )

                except httpx.HTTPStatusError as e:
                    if e.response.status_code in (429, 500, 502, 503, 504):
                        pass
                    else:
                        raise

            pending -= finished

            if pending:
                time.sleep(sleep_interval)

        if verbose:
            print("Done!")

    async def _await_for_resources(
        self,
        resource_ids: Sequence[str],
        get_status_fn: Callable[[str], Awaitable[ManagedIngestionStatusResponse]],
        resource_name: str,
        verbose: bool,
        raise_on_error: bool,
        sleep_interval: float,
    ) -> None:
"""
        Poll `get_status_fn` until every id in `resource_ids` is finished.

        Args:
            resource_ids: Iterable of resource ids to watch.
            get_status_fn: Callable that maps a resource id → ManagedIngestionStatus.
            resource_name: Text used in log / error messages: "file", "document", ….
            verbose: Print a progress bar.
            raise_on_error: Whether to raise on ManagedIngestionStatus.ERROR.
            sleep_interval: Seconds between polls (min 0.5 s to avoid rate-limits).

        """
        if not resource_ids:  # nothing to do
            return

        if verbose:
            print(
                f"Loading {resource_name}{'s'iflen(resource_ids)1else''}",
            )

        pending: set[str] = set(resource_ids)
        while pending:
            finished: set[str] = set()
            for rid in pending:
                try:
                    status_response = await get_status_fn(rid)
                    status = status_response.status
                    if status in (
                        ManagedIngestionStatus.NOT_STARTED,
                        ManagedIngestionStatus.IN_PROGRESS,
                    ):
                        continue  # still working

                    if status == ManagedIngestionStatus.ERROR:
                        if verbose:
                            print(
                                f"{resource_name.capitalize()} ingestion failed for {rid}"
                            )
                        if raise_on_error:
                            raise ValueError(
                                f"{resource_name.capitalize()} ingestion failed for {rid}"
                            )

                    finished.add(rid)
                    if verbose:
                        print(
                            f"{resource_name.capitalize()} ingestion finished for {rid}"
                        )

                except httpx.HTTPStatusError as e:
                    if e.response.status_code in (429, 500, 502, 503, 504):
                        pass
                    else:
                        raise

            pending -= finished

            if pending:
                await asyncio.sleep(sleep_interval)

        if verbose:
            print("Done!")

    def wait_for_completion(
        self,
        file_ids: Optional[Sequence[str]] = None,
        doc_ids: Optional[Sequence[str]] = None,
        verbose: bool = False,
        raise_on_partial_success: bool = False,
        raise_on_error: bool = False,
        sleep_interval: float = 1.0,
    ) -> Optional[ManagedIngestionStatusResponse]:
"""
        Block until the requested ingestion work is finished.

        - If `file_ids` is given → wait for those files.
        - If `doc_ids` is given → wait for those documents.
        - If neither is given → wait for the pipeline itself last so that retrieval works.
        - Always waits for the pipeline itself last so that retrieval works.

        Returns the final PipelineStatus response (or None if only waiting on
        files / documents).
        """
        # Batch of files (if any)
        if file_ids:
            self._wait_for_resources(
                file_ids,
                lambda fid: self._client.pipelines.get_pipeline_file_status(
                    pipeline_id=self.pipeline.id, file_id=fid
                ),
                resource_name="file",
                verbose=verbose,
                raise_on_error=raise_on_error,
                sleep_interval=sleep_interval,
            )

        # Batch of documents (if any)
        if doc_ids:
            self._wait_for_resources(
                doc_ids,
                lambda did: self._client.pipelines.get_pipeline_document_status(
                    pipeline_id=self.pipeline.id,
                    document_id=quote_plus(quote_plus(did)),
                ),
                resource_name="document",
                verbose=verbose,
                raise_on_error=raise_on_error,
                sleep_interval=sleep_interval,
            )

        # Finally, wait for the pipeline
        if verbose:
            print(f"Syncing pipeline {self.pipeline.id}")

        status_response: Optional[ManagedIngestionStatusResponse] = None
        while True:
            try:
                status_response = self._client.pipelines.get_pipeline_status(
                    pipeline_id=self.pipeline.id
                )
                status = status_response.status
            except httpx.HTTPStatusError as e:
                if e.response.status_code in (429, 500, 502, 503, 504):
                    time.sleep(sleep_interval)
                    continue
                else:
                    raise

            if status == ManagedIngestionStatus.ERROR or (
                raise_on_partial_success
                and status == ManagedIngestionStatus.PARTIAL_SUCCESS
            ):
                raise ValueError(
                    f"Pipeline ingestion failed for {self.pipeline.id}. "
                    f"Details: {status_response.json()}"
                )

            if status in (
                ManagedIngestionStatus.NOT_STARTED,
                ManagedIngestionStatus.IN_PROGRESS,
            ):
                if verbose:
                    print(".", end="")
                time.sleep(sleep_interval)
            else:
                if verbose:
                    print("Done!")

                return status_response

    async def await_for_completion(
        self,
        file_ids: Optional[Sequence[str]] = None,
        doc_ids: Optional[Sequence[str]] = None,
        verbose: bool = False,
        raise_on_partial_success: bool = False,
        raise_on_error: bool = False,
        sleep_interval: float = 1.0,
    ) -> Optional[ManagedIngestionStatusResponse]:
"""
        Block until the requested ingestion work is finished.

        - If `file_ids` is given → wait for those files.
        - If `doc_ids` is given → wait for those documents.
        - If neither is given → wait for the pipeline itself last so that retrieval works.
        - Always waits for the pipeline itself last so that retrieval works.

        Returns the final PipelineStatus response (or None if only waiting on
        files / documents).
        """
        # Batch of files (if any)
        if file_ids:
            await self._await_for_resources(
                file_ids,
                lambda fid: self._aclient.pipelines.get_pipeline_file_status(
                    pipeline_id=self.pipeline.id, file_id=fid
                ),
                resource_name="file",
                verbose=verbose,
                raise_on_error=raise_on_error,
                sleep_interval=sleep_interval,
            )

        # Batch of documents (if any)
        if doc_ids:
            await self._await_for_resources(
                doc_ids,
                lambda did: self._aclient.pipelines.get_pipeline_document_status(
                    pipeline_id=self.pipeline.id,
                    document_id=quote_plus(quote_plus(did)),
                ),
                resource_name="document",
                verbose=verbose,
                raise_on_error=raise_on_error,
                sleep_interval=sleep_interval,
            )

        # Finally, wait for the pipeline
        if verbose:
            print(f"Syncing pipeline {self.pipeline.id}")

        status_response: Optional[ManagedIngestionStatusResponse] = None
        while True:
            try:
                status_response = await self._aclient.pipelines.get_pipeline_status(
                    pipeline_id=self.pipeline.id
                )
                status = status_response.status
            except httpx.HTTPStatusError as e:
                if e.response.status_code in (429, 500, 502, 503, 504):
                    await asyncio.sleep(sleep_interval)
                    continue
                else:
                    raise

            if status == ManagedIngestionStatus.ERROR or (
                raise_on_partial_success
                and status == ManagedIngestionStatus.PARTIAL_SUCCESS
            ):
                raise ValueError(
                    f"Pipeline ingestion failed for {self.pipeline.id}. "
                    f"Details: {status_response.json()}"
                )

            if status in (
                ManagedIngestionStatus.NOT_STARTED,
                ManagedIngestionStatus.IN_PROGRESS,
            ):
                if verbose:
                    print(".", end="")
                await asyncio.sleep(sleep_interval)
            else:
                if verbose:
                    print("Done!")

                return status_response

    @classmethod
    def create_index(
        cls: Type["LlamaCloudIndex"],
        name: str,
        project_name: str = DEFAULT_PROJECT_NAME,
        organization_id: Optional[str] = None,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        app_url: Optional[str] = None,
        timeout: int = 60,
        verbose: bool = False,
        # ingestion configs
        embedding_config: Optional[PipelineCreateEmbeddingConfig] = None,
        transform_config: Optional[PipelineCreateTransformConfig] = None,
        llama_parse_parameters: Optional[LlamaParseParameters] = None,
        **kwargs: Any,
    ) -> "LlamaCloudIndex":
"""Create a new LlamaCloud managed index."""
        app_url = app_url or os.environ.get("LLAMA_CLOUD_APP_URL", DEFAULT_APP_URL)
        client = get_client(api_key, base_url, app_url, timeout)

        # create project if it doesn't exist
        project = client.projects.upsert_project(
            organization_id=organization_id, request=ProjectCreate(name=project_name)
        )
        if project.id is None:
            raise ValueError(f"Failed to create/get project {project_name}")

        if verbose:
            print(f"Created project {project.id} with name {project.name}")

        # create pipeline
        pipeline_create = PipelineCreate(
            name=name,
            pipeline_type=PipelineType.MANAGED,
            embedding_config=embedding_config,  # If it's None, the default embedding config will be used
            transform_config=transform_config or default_transform_config(),
            llama_parse_parameters=llama_parse_parameters or LlamaParseParameters(),
        )
        pipeline = client.pipelines.upsert_pipeline(
            project_id=project.id, request=pipeline_create
        )
        if pipeline.id is None:
            raise ValueError(f"Failed to create/get pipeline {name}")
        if verbose:
            print(f"Created pipeline {pipeline.id} with name {pipeline.name}")

        return cls(
            name,
            project_name=project.name,
            organization_id=project.organization_id,
            api_key=api_key,
            base_url=base_url,
            app_url=app_url,
            timeout=timeout,
            **kwargs,
        )

    @classmethod
    async def acreate_index(
        cls: Type["LlamaCloudIndex"],
        name: str,
        project_name: str = DEFAULT_PROJECT_NAME,
        organization_id: Optional[str] = None,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        app_url: Optional[str] = None,
        timeout: int = 60,
        verbose: bool = False,
        # ingestion configs
        embedding_config: Optional[PipelineCreateEmbeddingConfig] = None,
        transform_config: Optional[PipelineCreateTransformConfig] = None,
        llama_parse_parameters: Optional[LlamaParseParameters] = None,
        **kwargs: Any,
    ) -> "LlamaCloudIndex":
"""Create a new LlamaCloud managed index."""
        app_url = app_url or os.environ.get("LLAMA_CLOUD_APP_URL", DEFAULT_APP_URL)
        aclient = get_aclient(api_key, base_url, app_url, timeout)

        # create project if it doesn't exist
        project = await aclient.projects.upsert_project(
            organization_id=organization_id, request=ProjectCreate(name=project_name)
        )
        if project.id is None:
            raise ValueError(f"Failed to create/get project {project_name}")

        if verbose:
            print(f"Created project {project.id} with name {project.name}")

        # create pipeline
        pipeline_create = PipelineCreate(
            name=name,
            pipeline_type=PipelineType.MANAGED,
            embedding_config=embedding_config,  # If it's None, the default embedding config will be used
            transform_config=transform_config or default_transform_config(),
            llama_parse_parameters=llama_parse_parameters or LlamaParseParameters(),
        )
        pipeline = await aclient.pipelines.upsert_pipeline(
            project_id=project.id, request=pipeline_create
        )
        if pipeline.id is None:
            raise ValueError(f"Failed to create/get pipeline {name}")
        if verbose:
            print(f"Created pipeline {pipeline.id} with name {pipeline.name}")

        return cls(
            name,
            project_name=project.name,
            organization_id=project.organization_id,
            api_key=api_key,
            base_url=base_url,
            app_url=app_url,
            timeout=timeout,
            **kwargs,
        )

    @classmethod
    def from_documents(  # type: ignore
        cls: Type["LlamaCloudIndex"],
        documents: List[Document],
        name: str,
        project_name: str = DEFAULT_PROJECT_NAME,
        organization_id: Optional[str] = None,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        app_url: Optional[str] = None,
        timeout: int = 60,
        verbose: bool = False,
        raise_on_error: bool = False,
        # ingestion configs
        embedding_config: Optional[PipelineCreateEmbeddingConfig] = None,
        transform_config: Optional[PipelineCreateTransformConfig] = None,
        # deprecated
        transformations: Optional[List[TransformComponent]] = None,
        **kwargs: Any,
    ) -> "LlamaCloudIndex":
"""Build a LlamaCloud managed index from a sequence of documents."""
        index = cls.create_index(
            name=name,
            project_name=project_name,
            organization_id=organization_id,
            api_key=api_key,
            base_url=base_url,
            app_url=app_url,
            timeout=timeout,
            verbose=verbose,
            embedding_config=embedding_config,
            transform_config=transform_config,
        )

        app_url = app_url or os.environ.get("LLAMA_CLOUD_APP_URL", DEFAULT_APP_URL)
        client = get_client(api_key, base_url, app_url, timeout)

        # this kicks off document ingestion
        upserted_documents = client.pipelines.upsert_batch_pipeline_documents(
            pipeline_id=index.pipeline.id,
            request=[
                CloudDocumentCreate(
                    text=doc.text,
                    metadata=doc.metadata,
                    excluded_embed_metadata_keys=doc.excluded_embed_metadata_keys,
                    excluded_llm_metadata_keys=doc.excluded_llm_metadata_keys,
                    id=doc.id_,
                )
                for doc in documents
            ],
        )

        doc_ids = [doc.id for doc in upserted_documents]
        index.wait_for_completion(
            doc_ids=doc_ids, verbose=verbose, raise_on_error=raise_on_error
        )

        print(
            f"Find your index at {app_url}/project/{index.project.id}/deploy/{index.pipeline.id}"
        )

        return index

    def as_retriever(self, **kwargs: Any) -> BaseRetriever:
"""Return a Retriever for this managed index."""
        from llama_index.indices.managed.llama_cloud.retriever import (
            LlamaCloudRetriever,
        )

        similarity_top_k = kwargs.pop("similarity_top_k", None)
        dense_similarity_top_k = kwargs.pop("dense_similarity_top_k", None)
        if similarity_top_k is not None:
            dense_similarity_top_k = similarity_top_k

        return LlamaCloudRetriever(
            project_id=self.project.id,
            pipeline_id=self.pipeline.id,
            api_key=self._api_key,
            base_url=self._base_url,
            app_url=self._app_url,
            timeout=self._timeout,
            organization_id=self.organization_id,
            dense_similarity_top_k=dense_similarity_top_k,
            httpx_client=self._httpx_client,
            async_httpx_client=self._async_httpx_client,
            **kwargs,
        )

    def as_query_engine(self, **kwargs: Any) -> BaseQueryEngine:
        from llama_index.core.query_engine.retriever_query_engine import (
            RetrieverQueryEngine,
        )

        kwargs["retriever"] = self.as_retriever(**kwargs)
        return RetrieverQueryEngine.from_args(**kwargs)

    @property
    def ref_doc_info(self, batch_size: int = 100) -> Dict[str, RefDocInfo]:
"""Retrieve a dict mapping of ingested documents and their metadata. The nodes list is empty."""
        pipeline_id = self.pipeline.id
        pipeline_documents: List[CloudDocument] = []
        skip = 0
        limit = batch_size
        while True:
            batch = self._client.pipelines.list_pipeline_documents(
                pipeline_id=pipeline_id,
                skip=skip,
                limit=limit,
            )
            if not batch:
                break
            pipeline_documents.extend(batch)
            skip += limit
        return {
            doc.id: RefDocInfo(metadata=doc.metadata, node_ids=[])
            for doc in pipeline_documents
        }

    def insert(
        self, document: Document, verbose: bool = False, **insert_kwargs: Any
    ) -> None:
"""Insert a document."""
        with self._callback_manager.as_trace("insert"):
            upserted_documents = self._client.pipelines.create_batch_pipeline_documents(
                pipeline_id=self.pipeline.id,
                request=[
                    CloudDocumentCreate(
                        text=document.text,
                        metadata=document.metadata,
                        excluded_embed_metadata_keys=document.excluded_embed_metadata_keys,
                        excluded_llm_metadata_keys=document.excluded_llm_metadata_keys,
                        id=document.id_,
                    )
                ],
            )
            upserted_document = upserted_documents[0]
            self.wait_for_completion(
                doc_ids=[upserted_document.id], verbose=verbose, raise_on_error=True
            )

    async def ainsert(
        self, document: Document, verbose: bool = False, **insert_kwargs: Any
    ) -> None:
"""Insert a document."""
        with self._callback_manager.as_trace("insert"):
            upserted_documents = await self._aclient.pipelines.create_batch_pipeline_documents(
                pipeline_id=self.pipeline.id,
                request=[
                    CloudDocumentCreate(
                        text=document.text,
                        metadata=document.metadata,
                        excluded_embed_metadata_keys=document.excluded_embed_metadata_keys,
                        excluded_llm_metadata_keys=document.excluded_llm_metadata_keys,
                        id=document.id_,
                    )
                ],
            )
            upserted_document = upserted_documents[0]
            await self.await_for_completion(
                doc_ids=[upserted_document.id], verbose=verbose, raise_on_error=True
            )

    def update_ref_doc(
        self, document: Document, verbose: bool = False, **update_kwargs: Any
    ) -> None:
"""Upserts a document and its corresponding nodes."""
        with self._callback_manager.as_trace("update"):
            upserted_documents = self._client.pipelines.upsert_batch_pipeline_documents(
                pipeline_id=self.pipeline.id,
                request=[
                    CloudDocumentCreate(
                        text=document.text,
                        metadata=document.metadata,
                        excluded_embed_metadata_keys=document.excluded_embed_metadata_keys,
                        excluded_llm_metadata_keys=document.excluded_llm_metadata_keys,
                        id=document.id_,
                    )
                ],
            )
            upserted_document = upserted_documents[0]
            self.wait_for_completion(
                doc_ids=[upserted_document.id], verbose=verbose, raise_on_error=True
            )

    async def aupdate_ref_doc(
        self, document: Document, verbose: bool = False, **update_kwargs: Any
    ) -> None:
"""Upserts a document and its corresponding nodes."""
        with self._callback_manager.as_trace("update"):
            upserted_documents = await self._aclient.pipelines.upsert_batch_pipeline_documents(
                pipeline_id=self.pipeline.id,
                request=[
                    CloudDocumentCreate(
                        text=document.text,
                        metadata=document.metadata,
                        excluded_embed_metadata_keys=document.excluded_embed_metadata_keys,
                        excluded_llm_metadata_keys=document.excluded_llm_metadata_keys,
                        id=document.id_,
                    )
                ],
            )
            upserted_document = upserted_documents[0]
            await self.await_for_completion(
                doc_ids=[upserted_document.id], verbose=verbose, raise_on_error=True
            )

    def refresh_ref_docs(
        self, documents: Sequence[Document], **update_kwargs: Any
    ) -> List[bool]:
"""Refresh an index with documents that have changed."""
        with self._callback_manager.as_trace("refresh"):
            upserted_documents = self._client.pipelines.upsert_batch_pipeline_documents(
                pipeline_id=self.pipeline.id,
                request=[
                    CloudDocumentCreate(
                        text=doc.text,
                        metadata=doc.metadata,
                        excluded_embed_metadata_keys=doc.excluded_embed_metadata_keys,
                        excluded_llm_metadata_keys=doc.excluded_llm_metadata_keys,
                        id=doc.id_,
                    )
                    for doc in documents
                ],
            )
            doc_ids = [doc.id for doc in upserted_documents]
            self.wait_for_completion(doc_ids=doc_ids, verbose=True, raise_on_error=True)
            return [True] * len(doc_ids)

    async def arefresh_ref_docs(
        self, documents: Sequence[Document], **update_kwargs: Any
    ) -> List[bool]:
"""Refresh an index with documents that have changed."""
        with self._callback_manager.as_trace("refresh"):
            upserted_documents = await self._aclient.pipelines.upsert_batch_pipeline_documents(
                pipeline_id=self.pipeline.id,
                request=[
                    CloudDocumentCreate(
                        text=doc.text,
                        metadata=doc.metadata,
                        excluded_embed_metadata_keys=doc.excluded_embed_metadata_keys,
                        excluded_llm_metadata_keys=doc.excluded_llm_metadata_keys,
                        id=doc.id_,
                    )
                    for doc in documents
                ],
            )
            doc_ids = [doc.id for doc in upserted_documents]
            await self.await_for_completion(
                doc_ids=doc_ids, verbose=True, raise_on_error=True
            )
            return [True] * len(doc_ids)

    def delete_ref_doc(
        self,
        ref_doc_id: str,
        delete_from_docstore: bool = False,
        verbose: bool = False,
        raise_if_not_found: bool = False,
        **delete_kwargs: Any,
    ) -> None:
"""Delete a document and its nodes by using ref_doc_id."""
        try:
            # we have to quote the ref_doc_id twice because it is used as a path parameter
            self._client.pipelines.delete_pipeline_document(
                pipeline_id=self.pipeline.id,
                document_id=quote_plus(quote_plus(ref_doc_id)),
            )
        except ApiError as e:
            if e.status_code == 404 and not raise_if_not_found:
                logger.warning(f"ref_doc_id {ref_doc_id} not found, nothing deleted.")
            else:
                raise

        # we have to wait for the pipeline instead of the document, because the document is already deleted
        self.wait_for_completion(verbose=verbose, raise_on_partial_success=False)

    async def adelete_ref_doc(
        self,
        ref_doc_id: str,
        delete_from_docstore: bool = False,
        verbose: bool = False,
        raise_if_not_found: bool = False,
        **delete_kwargs: Any,
    ) -> None:
"""Delete a document and its nodes by using ref_doc_id."""
        try:
            # we have to quote the ref_doc_id twice because it is used as a path parameter
            await self._aclient.pipelines.delete_pipeline_document(
                pipeline_id=self.pipeline.id,
                document_id=quote_plus(quote_plus(ref_doc_id)),
            )
        except ApiError as e:
            if e.status_code == 404 and not raise_if_not_found:
                logger.warning(f"ref_doc_id {ref_doc_id} not found, nothing deleted.")
            else:
                raise

        # we have to wait for the pipeline instead of the document, because the document is already deleted
        await self.await_for_completion(verbose=verbose, raise_on_partial_success=False)

    def upload_file(
        self,
        file_path: str,
        verbose: bool = False,
        wait_for_ingestion: bool = True,
        raise_on_error: bool = False,
    ) -> str:
"""Upload a file to the index."""
        with open(file_path, "rb") as f:
            file = self._client.files.upload_file(
                project_id=self.project.id, upload_file=f
            )
            if verbose:
                print(f"Uploaded file {file.id} with name {file.name}")

        # Add file to pipeline
        pipeline_file_create = PipelineFileCreate(file_id=file.id)
        self._client.pipelines.add_files_to_pipeline_api(
            pipeline_id=self.pipeline.id, request=[pipeline_file_create]
        )

        if wait_for_ingestion:
            self.wait_for_completion(
                file_ids=[file.id], verbose=verbose, raise_on_error=raise_on_error
            )
        return file.id

    async def aupload_file(
        self,
        file_path: str,
        verbose: bool = False,
        wait_for_ingestion: bool = True,
        raise_on_error: bool = False,
    ) -> str:
"""Upload a file to the index."""
        with open(file_path, "rb") as f:
            file = await self._aclient.files.upload_file(
                project_id=self.project.id, upload_file=f
            )
            if verbose:
                print(f"Uploaded file {file.id} with name {file.name}")

        # Add file to pipeline
        pipeline_file_create = PipelineFileCreate(file_id=file.id)
        await self._aclient.pipelines.add_files_to_pipeline_api(
            pipeline_id=self.pipeline.id, request=[pipeline_file_create]
        )

        if wait_for_ingestion:
            await self.await_for_completion(
                file_ids=[file.id], verbose=verbose, raise_on_error=raise_on_error
            )

        return file.id

    def upload_file_from_url(
        self,
        file_name: str,
        url: str,
        proxy_url: Optional[str] = None,
        request_headers: Optional[Dict[str, str]] = None,
        verify_ssl: bool = True,
        follow_redirects: bool = True,
        verbose: bool = False,
        wait_for_ingestion: bool = True,
        raise_on_error: bool = False,
    ) -> str:
"""Upload a file from a URL to the index."""
        file = self._client.files.upload_file_from_url(
            project_id=self.project.id,
            name=file_name,
            url=url,
            proxy_url=proxy_url,
            request_headers=request_headers,
            verify_ssl=verify_ssl,
            follow_redirects=follow_redirects,
        )
        if verbose:
            print(f"Uploaded file {file.id} with ID {file.id}")

        # Add file to pipeline
        pipeline_file_create = PipelineFileCreate(file_id=file.id)
        self._client.pipelines.add_files_to_pipeline_api(
            pipeline_id=self.pipeline.id, request=[pipeline_file_create]
        )

        if wait_for_ingestion:
            self.wait_for_completion(
                file_ids=[file.id], verbose=verbose, raise_on_error=raise_on_error
            )
        return file.id

    async def aupload_file_from_url(
        self,
        file_name: str,
        url: str,
        proxy_url: Optional[str] = None,
        request_headers: Optional[Dict[str, str]] = None,
        verify_ssl: bool = True,
        follow_redirects: bool = True,
        verbose: bool = False,
        wait_for_ingestion: bool = True,
        raise_on_error: bool = False,
    ) -> str:
"""Upload a file from a URL to the index."""
        file = await self._aclient.files.upload_file_from_url(
            project_id=self.project.id,
            name=file_name,
            url=url,
            proxy_url=proxy_url,
            request_headers=request_headers,
            verify_ssl=verify_ssl,
            follow_redirects=follow_redirects,
        )
        if verbose:
            print(f"Uploaded file {file.id} with ID {file.id}")

        # Add file to pipeline
        pipeline_file_create = PipelineFileCreate(file_id=file.id)
        await self._aclient.pipelines.add_files_to_pipeline_api(
            pipeline_id=self.pipeline.id, request=[pipeline_file_create]
        )

        if wait_for_ingestion:
            await self.await_for_completion(
                file_ids=[file.id], verbose=verbose, raise_on_error=raise_on_error
            )

        return file.id

    # Nodes related methods (not implemented for LlamaCloudIndex)

    def _insert(self, nodes: Sequence[BaseNode], **insert_kwargs: Any) -> None:
"""Index-specific logic for inserting nodes to the index struct."""
        raise NotImplementedError("_insert not implemented for LlamaCloudIndex.")

    def build_index_from_nodes(self, nodes: Sequence[BaseNode]) -> None:
"""Build the index from nodes."""
        raise NotImplementedError(
            "build_index_from_nodes not implemented for LlamaCloudIndex."
        )

    def insert_nodes(self, nodes: Sequence[BaseNode], **insert_kwargs: Any) -> None:
"""Insert a set of nodes."""
        raise NotImplementedError("insert_nodes not implemented for LlamaCloudIndex.")

    def delete_nodes(
        self,
        node_ids: List[str],
        delete_from_docstore: bool = False,
        **delete_kwargs: Any,
    ) -> None:
"""Delete a set of nodes."""
        raise NotImplementedError("delete_nodes not implemented for LlamaCloudIndex.")

```
  
---|---  
###  id `property` [#](https://developers.llamaindex.ai/python/framework-api-reference/indices/llama_cloud/#llama_index.indices.managed.llama_cloud.LlamaCloudIndex.id "Permanent link")
```
id: 

```

Return the pipeline (aka index) ID.
###  ref_doc_info `property` [#](https://developers.llamaindex.ai/python/framework-api-reference/indices/llama_cloud/#llama_index.indices.managed.llama_cloud.LlamaCloudIndex.ref_doc_info "Permanent link")
```
ref_doc_info: [, ]

```

Retrieve a dict mapping of ingested documents and their metadata. The nodes list is empty.
###  wait_for_completion [#](https://developers.llamaindex.ai/python/framework-api-reference/indices/llama_cloud/#llama_index.indices.managed.llama_cloud.LlamaCloudIndex.wait_for_completion "Permanent link")
```
wait_for_completion(file_ids: Optional[Sequence[]] = None, doc_ids: Optional[Sequence[]] = None, verbose:  = False, raise_on_partial_success:  = False, raise_on_error:  = False, sleep_interval: float = 1.0) -> Optional[ManagedIngestionStatusResponse]

```

Block until the requested ingestion work is finished.
  * If `file_ids` is given → wait for those files.
  * If `doc_ids` is given → wait for those documents.
  * If neither is given → wait for the pipeline itself last so that retrieval works.
  * Always waits for the pipeline itself last so that retrieval works.


Returns the final PipelineStatus response (or None if only waiting on files / documents).
Source code in `llama_index/indices/managed/llama_cloud/base.py`
```
327
328
329
330
331
332
333
334
335
336
337
338
339
340
341
342
343
344
345
346
347
348
349
350
351
352
353
354
355
356
357
358
359
360
361
362
363
364
365
366
367
368
369
370
371
372
373
374
375
376
377
378
379
380
381
382
383
384
385
386
387
388
389
390
391
392
393
394
395
396
397
398
399
400
401
402
403
404
405
406
407
408
409
410
411
412
```
| ```
def wait_for_completion(
    self,
    file_ids: Optional[Sequence[str]] = None,
    doc_ids: Optional[Sequence[str]] = None,
    verbose: bool = False,
    raise_on_partial_success: bool = False,
    raise_on_error: bool = False,
    sleep_interval: float = 1.0,
) -> Optional[ManagedIngestionStatusResponse]:
"""
    Block until the requested ingestion work is finished.

    - If `file_ids` is given → wait for those files.
    - If `doc_ids` is given → wait for those documents.
    - If neither is given → wait for the pipeline itself last so that retrieval works.
    - Always waits for the pipeline itself last so that retrieval works.

    Returns the final PipelineStatus response (or None if only waiting on
    files / documents).
    """
    # Batch of files (if any)
    if file_ids:
        self._wait_for_resources(
            file_ids,
            lambda fid: self._client.pipelines.get_pipeline_file_status(
                pipeline_id=self.pipeline.id, file_id=fid
            ),
            resource_name="file",
            verbose=verbose,
            raise_on_error=raise_on_error,
            sleep_interval=sleep_interval,
        )

    # Batch of documents (if any)
    if doc_ids:
        self._wait_for_resources(
            doc_ids,
            lambda did: self._client.pipelines.get_pipeline_document_status(
                pipeline_id=self.pipeline.id,
                document_id=quote_plus(quote_plus(did)),
            ),
            resource_name="document",
            verbose=verbose,
            raise_on_error=raise_on_error,
            sleep_interval=sleep_interval,
        )

    # Finally, wait for the pipeline
    if verbose:
        print(f"Syncing pipeline {self.pipeline.id}")

    status_response: Optional[ManagedIngestionStatusResponse] = None
    while True:
        try:
            status_response = self._client.pipelines.get_pipeline_status(
                pipeline_id=self.pipeline.id
            )
            status = status_response.status
        except httpx.HTTPStatusError as e:
            if e.response.status_code in (429, 500, 502, 503, 504):
                time.sleep(sleep_interval)
                continue
            else:
                raise

        if status == ManagedIngestionStatus.ERROR or (
            raise_on_partial_success
            and status == ManagedIngestionStatus.PARTIAL_SUCCESS
        ):
            raise ValueError(
                f"Pipeline ingestion failed for {self.pipeline.id}. "
                f"Details: {status_response.json()}"
            )

        if status in (
            ManagedIngestionStatus.NOT_STARTED,
            ManagedIngestionStatus.IN_PROGRESS,
        ):
            if verbose:
                print(".", end="")
            time.sleep(sleep_interval)
        else:
            if verbose:
                print("Done!")

            return status_response

```
  
---|---  
###  await_for_completion `async` [#](https://developers.llamaindex.ai/python/framework-api-reference/indices/llama_cloud/#llama_index.indices.managed.llama_cloud.LlamaCloudIndex.await_for_completion "Permanent link")
```
await_for_completion(file_ids: Optional[Sequence[]] = None, doc_ids: Optional[Sequence[]] = None, verbose:  = False, raise_on_partial_success:  = False, raise_on_error:  = False, sleep_interval: float = 1.0) -> Optional[ManagedIngestionStatusResponse]

```

Block until the requested ingestion work is finished.
  * If `file_ids` is given → wait for those files.
  * If `doc_ids` is given → wait for those documents.
  * If neither is given → wait for the pipeline itself last so that retrieval works.
  * Always waits for the pipeline itself last so that retrieval works.


Returns the final PipelineStatus response (or None if only waiting on files / documents).
Source code in `llama_index/indices/managed/llama_cloud/base.py`
```
414
415
416
417
418
419
420
421
422
423
424
425
426
427
428
429
430
431
432
433
434
435
436
437
438
439
440
441
442
443
444
445
446
447
448
449
450
451
452
453
454
455
456
457
458
459
460
461
462
463
464
465
466
467
468
469
470
471
472
473
474
475
476
477
478
479
480
481
482
483
484
485
486
487
488
489
490
491
492
493
494
495
496
497
498
499
```
| ```
async def await_for_completion(
    self,
    file_ids: Optional[Sequence[str]] = None,
    doc_ids: Optional[Sequence[str]] = None,
    verbose: bool = False,
    raise_on_partial_success: bool = False,
    raise_on_error: bool = False,
    sleep_interval: float = 1.0,
) -> Optional[ManagedIngestionStatusResponse]:
"""
    Block until the requested ingestion work is finished.

    - If `file_ids` is given → wait for those files.
    - If `doc_ids` is given → wait for those documents.
    - If neither is given → wait for the pipeline itself last so that retrieval works.
    - Always waits for the pipeline itself last so that retrieval works.

    Returns the final PipelineStatus response (or None if only waiting on
    files / documents).
    """
    # Batch of files (if any)
    if file_ids:
        await self._await_for_resources(
            file_ids,
            lambda fid: self._aclient.pipelines.get_pipeline_file_status(
                pipeline_id=self.pipeline.id, file_id=fid
            ),
            resource_name="file",
            verbose=verbose,
            raise_on_error=raise_on_error,
            sleep_interval=sleep_interval,
        )

    # Batch of documents (if any)
    if doc_ids:
        await self._await_for_resources(
            doc_ids,
            lambda did: self._aclient.pipelines.get_pipeline_document_status(
                pipeline_id=self.pipeline.id,
                document_id=quote_plus(quote_plus(did)),
            ),
            resource_name="document",
            verbose=verbose,
            raise_on_error=raise_on_error,
            sleep_interval=sleep_interval,
        )

    # Finally, wait for the pipeline
    if verbose:
        print(f"Syncing pipeline {self.pipeline.id}")

    status_response: Optional[ManagedIngestionStatusResponse] = None
    while True:
        try:
            status_response = await self._aclient.pipelines.get_pipeline_status(
                pipeline_id=self.pipeline.id
            )
            status = status_response.status
        except httpx.HTTPStatusError as e:
            if e.response.status_code in (429, 500, 502, 503, 504):
                await asyncio.sleep(sleep_interval)
                continue
            else:
                raise

        if status == ManagedIngestionStatus.ERROR or (
            raise_on_partial_success
            and status == ManagedIngestionStatus.PARTIAL_SUCCESS
        ):
            raise ValueError(
                f"Pipeline ingestion failed for {self.pipeline.id}. "
                f"Details: {status_response.json()}"
            )

        if status in (
            ManagedIngestionStatus.NOT_STARTED,
            ManagedIngestionStatus.IN_PROGRESS,
        ):
            if verbose:
                print(".", end="")
            await asyncio.sleep(sleep_interval)
        else:
            if verbose:
                print("Done!")

            return status_response

```
  
---|---  
###  create_index `classmethod` [#](https://developers.llamaindex.ai/python/framework-api-reference/indices/llama_cloud/#llama_index.indices.managed.llama_cloud.LlamaCloudIndex.create_index "Permanent link")
```
create_index(name: , project_name:  = DEFAULT_PROJECT_NAME, organization_id: Optional[] = None, api_key: Optional[] = None, base_url: Optional[] = None, app_url: Optional[] = None, timeout:  = 60, verbose:  = False, embedding_config: Optional[PipelineCreateEmbeddingConfig] = None, transform_config: Optional[PipelineCreateTransformConfig] = None, llama_parse_parameters: Optional[LlamaParseParameters] = None, **kwargs: ) -> 

```

Create a new LlamaCloud managed index.
Source code in `llama_index/indices/managed/llama_cloud/base.py`
```
501
502
503
504
505
506
507
508
509
510
511
512
513
514
515
516
517
518
519
520
521
522
523
524
525
526
527
528
529
530
531
532
533
534
535
536
537
538
539
540
541
542
543
544
545
546
547
548
549
550
551
552
553
554
555
556
557
```
| ```
@classmethod
def create_index(
    cls: Type["LlamaCloudIndex"],
    name: str,
    project_name: str = DEFAULT_PROJECT_NAME,
    organization_id: Optional[str] = None,
    api_key: Optional[str] = None,
    base_url: Optional[str] = None,
    app_url: Optional[str] = None,
    timeout: int = 60,
    verbose: bool = False,
    # ingestion configs
    embedding_config: Optional[PipelineCreateEmbeddingConfig] = None,
    transform_config: Optional[PipelineCreateTransformConfig] = None,
    llama_parse_parameters: Optional[LlamaParseParameters] = None,
    **kwargs: Any,
) -> "LlamaCloudIndex":
"""Create a new LlamaCloud managed index."""
    app_url = app_url or os.environ.get("LLAMA_CLOUD_APP_URL", DEFAULT_APP_URL)
    client = get_client(api_key, base_url, app_url, timeout)

    # create project if it doesn't exist
    project = client.projects.upsert_project(
        organization_id=organization_id, request=ProjectCreate(name=project_name)
    )
    if project.id is None:
        raise ValueError(f"Failed to create/get project {project_name}")

    if verbose:
        print(f"Created project {project.id} with name {project.name}")

    # create pipeline
    pipeline_create = PipelineCreate(
        name=name,
        pipeline_type=PipelineType.MANAGED,
        embedding_config=embedding_config,  # If it's None, the default embedding config will be used
        transform_config=transform_config or default_transform_config(),
        llama_parse_parameters=llama_parse_parameters or LlamaParseParameters(),
    )
    pipeline = client.pipelines.upsert_pipeline(
        project_id=project.id, request=pipeline_create
    )
    if pipeline.id is None:
        raise ValueError(f"Failed to create/get pipeline {name}")
    if verbose:
        print(f"Created pipeline {pipeline.id} with name {pipeline.name}")

    return cls(
        name,
        project_name=project.name,
        organization_id=project.organization_id,
        api_key=api_key,
        base_url=base_url,
        app_url=app_url,
        timeout=timeout,
        **kwargs,
    )

```
  
---|---  
###  acreate_index `async` `classmethod` [#](https://developers.llamaindex.ai/python/framework-api-reference/indices/llama_cloud/#llama_index.indices.managed.llama_cloud.LlamaCloudIndex.acreate_index "Permanent link")
```
acreate_index(name: , project_name:  = DEFAULT_PROJECT_NAME, organization_id: Optional[] = None, api_key: Optional[] = None, base_url: Optional[] = None, app_url: Optional[] = None, timeout:  = 60, verbose:  = False, embedding_config: Optional[PipelineCreateEmbeddingConfig] = None, transform_config: Optional[PipelineCreateTransformConfig] = None, llama_parse_parameters: Optional[LlamaParseParameters] = None, **kwargs: ) -> 

```

Create a new LlamaCloud managed index.
Source code in `llama_index/indices/managed/llama_cloud/base.py`
```
559
560
561
562
563
564
565
566
567
568
569
570
571
572
573
574
575
576
577
578
579
580
581
582
583
584
585
586
587
588
589
590
591
592
593
594
595
596
597
598
599
600
601
602
603
604
605
606
607
608
609
610
611
612
613
614
615
```
| ```
@classmethod
async def acreate_index(
    cls: Type["LlamaCloudIndex"],
    name: str,
    project_name: str = DEFAULT_PROJECT_NAME,
    organization_id: Optional[str] = None,
    api_key: Optional[str] = None,
    base_url: Optional[str] = None,
    app_url: Optional[str] = None,
    timeout: int = 60,
    verbose: bool = False,
    # ingestion configs
    embedding_config: Optional[PipelineCreateEmbeddingConfig] = None,
    transform_config: Optional[PipelineCreateTransformConfig] = None,
    llama_parse_parameters: Optional[LlamaParseParameters] = None,
    **kwargs: Any,
) -> "LlamaCloudIndex":
"""Create a new LlamaCloud managed index."""
    app_url = app_url or os.environ.get("LLAMA_CLOUD_APP_URL", DEFAULT_APP_URL)
    aclient = get_aclient(api_key, base_url, app_url, timeout)

    # create project if it doesn't exist
    project = await aclient.projects.upsert_project(
        organization_id=organization_id, request=ProjectCreate(name=project_name)
    )
    if project.id is None:
        raise ValueError(f"Failed to create/get project {project_name}")

    if verbose:
        print(f"Created project {project.id} with name {project.name}")

    # create pipeline
    pipeline_create = PipelineCreate(
        name=name,
        pipeline_type=PipelineType.MANAGED,
        embedding_config=embedding_config,  # If it's None, the default embedding config will be used
        transform_config=transform_config or default_transform_config(),
        llama_parse_parameters=llama_parse_parameters or LlamaParseParameters(),
    )
    pipeline = await aclient.pipelines.upsert_pipeline(
        project_id=project.id, request=pipeline_create
    )
    if pipeline.id is None:
        raise ValueError(f"Failed to create/get pipeline {name}")
    if verbose:
        print(f"Created pipeline {pipeline.id} with name {pipeline.name}")

    return cls(
        name,
        project_name=project.name,
        organization_id=project.organization_id,
        api_key=api_key,
        base_url=base_url,
        app_url=app_url,
        timeout=timeout,
        **kwargs,
    )

```
  
---|---  
###  from_documents `classmethod` [#](https://developers.llamaindex.ai/python/framework-api-reference/indices/llama_cloud/#llama_index.indices.managed.llama_cloud.LlamaCloudIndex.from_documents "Permanent link")
```
from_documents(documents: [], name: , project_name:  = DEFAULT_PROJECT_NAME, organization_id: Optional[] = None, api_key: Optional[] = None, base_url: Optional[] = None, app_url: Optional[] = None, timeout:  = 60, verbose:  = False, raise_on_error:  = False, embedding_config: Optional[PipelineCreateEmbeddingConfig] = None, transform_config: Optional[PipelineCreateTransformConfig] = None, transformations: Optional[[]] = None, **kwargs: ) -> 

```

Build a LlamaCloud managed index from a sequence of documents.
Source code in `llama_index/indices/managed/llama_cloud/base.py`
```
617
618
619
620
621
622
623
624
625
626
627
628
629
630
631
632
633
634
635
636
637
638
639
640
641
642
643
644
645
646
647
648
649
650
651
652
653
654
655
656
657
658
659
660
661
662
663
664
665
666
667
668
669
670
671
672
673
674
675
676
677
678
```
| ```
@classmethod
def from_documents(  # type: ignore
    cls: Type["LlamaCloudIndex"],
    documents: List[Document],
    name: str,
    project_name: str = DEFAULT_PROJECT_NAME,
    organization_id: Optional[str] = None,
    api_key: Optional[str] = None,
    base_url: Optional[str] = None,
    app_url: Optional[str] = None,
    timeout: int = 60,
    verbose: bool = False,
    raise_on_error: bool = False,
    # ingestion configs
    embedding_config: Optional[PipelineCreateEmbeddingConfig] = None,
    transform_config: Optional[PipelineCreateTransformConfig] = None,
    # deprecated
    transformations: Optional[List[TransformComponent]] = None,
    **kwargs: Any,
) -> "LlamaCloudIndex":
"""Build a LlamaCloud managed index from a sequence of documents."""
    index = cls.create_index(
        name=name,
        project_name=project_name,
        organization_id=organization_id,
        api_key=api_key,
        base_url=base_url,
        app_url=app_url,
        timeout=timeout,
        verbose=verbose,
        embedding_config=embedding_config,
        transform_config=transform_config,
    )

    app_url = app_url or os.environ.get("LLAMA_CLOUD_APP_URL", DEFAULT_APP_URL)
    client = get_client(api_key, base_url, app_url, timeout)

    # this kicks off document ingestion
    upserted_documents = client.pipelines.upsert_batch_pipeline_documents(
        pipeline_id=index.pipeline.id,
        request=[
            CloudDocumentCreate(
                text=doc.text,
                metadata=doc.metadata,
                excluded_embed_metadata_keys=doc.excluded_embed_metadata_keys,
                excluded_llm_metadata_keys=doc.excluded_llm_metadata_keys,
                id=doc.id_,
            )
            for doc in documents
        ],
    )

    doc_ids = [doc.id for doc in upserted_documents]
    index.wait_for_completion(
        doc_ids=doc_ids, verbose=verbose, raise_on_error=raise_on_error
    )

    print(
        f"Find your index at {app_url}/project/{index.project.id}/deploy/{index.pipeline.id}"
    )

    return index

```
  
---|---  
###  as_retriever [#](https://developers.llamaindex.ai/python/framework-api-reference/indices/llama_cloud/#llama_index.indices.managed.llama_cloud.LlamaCloudIndex.as_retriever "Permanent link")
```
as_retriever(**kwargs: ) -> 

```

Return a Retriever for this managed index.
Source code in `llama_index/indices/managed/llama_cloud/base.py`
```
680
681
682
683
684
685
686
687
688
689
690
691
692
693
694
695
696
697
698
699
700
701
702
703
```
| ```
def as_retriever(self, **kwargs: Any) -> BaseRetriever:
"""Return a Retriever for this managed index."""
    from llama_index.indices.managed.llama_cloud.retriever import (
        LlamaCloudRetriever,
    )

    similarity_top_k = kwargs.pop("similarity_top_k", None)
    dense_similarity_top_k = kwargs.pop("dense_similarity_top_k", None)
    if similarity_top_k is not None:
        dense_similarity_top_k = similarity_top_k

    return LlamaCloudRetriever(
        project_id=self.project.id,
        pipeline_id=self.pipeline.id,
        api_key=self._api_key,
        base_url=self._base_url,
        app_url=self._app_url,
        timeout=self._timeout,
        organization_id=self.organization_id,
        dense_similarity_top_k=dense_similarity_top_k,
        httpx_client=self._httpx_client,
        async_httpx_client=self._async_httpx_client,
        **kwargs,
    )

```
  
---|---  
###  insert [#](https://developers.llamaindex.ai/python/framework-api-reference/indices/llama_cloud/#llama_index.indices.managed.llama_cloud.LlamaCloudIndex.insert "Permanent link")
```
insert(document: , verbose:  = False, **insert_kwargs: ) -> None

```

Insert a document.
Source code in `llama_index/indices/managed/llama_cloud/base.py`
```
735
736
737
738
739
740
741
742
743
744
745
746
747
748
749
750
751
752
753
754
755
```
| ```
def insert(
    self, document: Document, verbose: bool = False, **insert_kwargs: Any
) -> None:
"""Insert a document."""
    with self._callback_manager.as_trace("insert"):
        upserted_documents = self._client.pipelines.create_batch_pipeline_documents(
            pipeline_id=self.pipeline.id,
            request=[
                CloudDocumentCreate(
                    text=document.text,
                    metadata=document.metadata,
                    excluded_embed_metadata_keys=document.excluded_embed_metadata_keys,
                    excluded_llm_metadata_keys=document.excluded_llm_metadata_keys,
                    id=document.id_,
                )
            ],
        )
        upserted_document = upserted_documents[0]
        self.wait_for_completion(
            doc_ids=[upserted_document.id], verbose=verbose, raise_on_error=True
        )

```
  
---|---  
###  ainsert `async` [#](https://developers.llamaindex.ai/python/framework-api-reference/indices/llama_cloud/#llama_index.indices.managed.llama_cloud.LlamaCloudIndex.ainsert "Permanent link")
```
ainsert(document: , verbose:  = False, **insert_kwargs: ) -> None

```

Insert a document.
Source code in `llama_index/indices/managed/llama_cloud/base.py`
```
757
758
759
760
761
762
763
764
765
766
767
768
769
770
771
772
773
774
775
776
777
```
| ```
async def ainsert(
    self, document: Document, verbose: bool = False, **insert_kwargs: Any
) -> None:
"""Insert a document."""
    with self._callback_manager.as_trace("insert"):
        upserted_documents = await self._aclient.pipelines.create_batch_pipeline_documents(
            pipeline_id=self.pipeline.id,
            request=[
                CloudDocumentCreate(
                    text=document.text,
                    metadata=document.metadata,
                    excluded_embed_metadata_keys=document.excluded_embed_metadata_keys,
                    excluded_llm_metadata_keys=document.excluded_llm_metadata_keys,
                    id=document.id_,
                )
            ],
        )
        upserted_document = upserted_documents[0]
        await self.await_for_completion(
            doc_ids=[upserted_document.id], verbose=verbose, raise_on_error=True
        )

```
  
---|---  
###  update_ref_doc [#](https://developers.llamaindex.ai/python/framework-api-reference/indices/llama_cloud/#llama_index.indices.managed.llama_cloud.LlamaCloudIndex.update_ref_doc "Permanent link")
```
update_ref_doc(document: , verbose:  = False, **update_kwargs: ) -> None

```

Upserts a document and its corresponding nodes.
Source code in `llama_index/indices/managed/llama_cloud/base.py`
```
779
780
781
782
783
784
785
786
787
788
789
790
791
792
793
794
795
796
797
798
799
```
| ```
def update_ref_doc(
    self, document: Document, verbose: bool = False, **update_kwargs: Any
) -> None:
"""Upserts a document and its corresponding nodes."""
    with self._callback_manager.as_trace("update"):
        upserted_documents = self._client.pipelines.upsert_batch_pipeline_documents(
            pipeline_id=self.pipeline.id,
            request=[
                CloudDocumentCreate(
                    text=document.text,
                    metadata=document.metadata,
                    excluded_embed_metadata_keys=document.excluded_embed_metadata_keys,
                    excluded_llm_metadata_keys=document.excluded_llm_metadata_keys,
                    id=document.id_,
                )
            ],
        )
        upserted_document = upserted_documents[0]
        self.wait_for_completion(
            doc_ids=[upserted_document.id], verbose=verbose, raise_on_error=True
        )

```
  
---|---  
###  aupdate_ref_doc `async` [#](https://developers.llamaindex.ai/python/framework-api-reference/indices/llama_cloud/#llama_index.indices.managed.llama_cloud.LlamaCloudIndex.aupdate_ref_doc "Permanent link")
```
aupdate_ref_doc(document: , verbose:  = False, **update_kwargs: ) -> None

```

Upserts a document and its corresponding nodes.
Source code in `llama_index/indices/managed/llama_cloud/base.py`
```
801
802
803
804
805
806
807
808
809
810
811
812
813
814
815
816
817
818
819
820
821
```
| ```
async def aupdate_ref_doc(
    self, document: Document, verbose: bool = False, **update_kwargs: Any
) -> None:
"""Upserts a document and its corresponding nodes."""
    with self._callback_manager.as_trace("update"):
        upserted_documents = await self._aclient.pipelines.upsert_batch_pipeline_documents(
            pipeline_id=self.pipeline.id,
            request=[
                CloudDocumentCreate(
                    text=document.text,
                    metadata=document.metadata,
                    excluded_embed_metadata_keys=document.excluded_embed_metadata_keys,
                    excluded_llm_metadata_keys=document.excluded_llm_metadata_keys,
                    id=document.id_,
                )
            ],
        )
        upserted_document = upserted_documents[0]
        await self.await_for_completion(
            doc_ids=[upserted_document.id], verbose=verbose, raise_on_error=True
        )

```
  
---|---  
###  refresh_ref_docs [#](https://developers.llamaindex.ai/python/framework-api-reference/indices/llama_cloud/#llama_index.indices.managed.llama_cloud.LlamaCloudIndex.refresh_ref_docs "Permanent link")
```
refresh_ref_docs(documents: Sequence[], **update_kwargs: ) -> []

```

Refresh an index with documents that have changed.
Source code in `llama_index/indices/managed/llama_cloud/base.py`
```
823
824
825
826
827
828
829
830
831
832
833
834
835
836
837
838
839
840
841
842
843
```
| ```
def refresh_ref_docs(
    self, documents: Sequence[Document], **update_kwargs: Any
) -> List[bool]:
"""Refresh an index with documents that have changed."""
    with self._callback_manager.as_trace("refresh"):
        upserted_documents = self._client.pipelines.upsert_batch_pipeline_documents(
            pipeline_id=self.pipeline.id,
            request=[
                CloudDocumentCreate(
                    text=doc.text,
                    metadata=doc.metadata,
                    excluded_embed_metadata_keys=doc.excluded_embed_metadata_keys,
                    excluded_llm_metadata_keys=doc.excluded_llm_metadata_keys,
                    id=doc.id_,
                )
                for doc in documents
            ],
        )
        doc_ids = [doc.id for doc in upserted_documents]
        self.wait_for_completion(doc_ids=doc_ids, verbose=True, raise_on_error=True)
        return [True] * len(doc_ids)

```
  
---|---  
###  arefresh_ref_docs `async` [#](https://developers.llamaindex.ai/python/framework-api-reference/indices/llama_cloud/#llama_index.indices.managed.llama_cloud.LlamaCloudIndex.arefresh_ref_docs "Permanent link")
```
arefresh_ref_docs(documents: Sequence[], **update_kwargs: ) -> []

```

Refresh an index with documents that have changed.
Source code in `llama_index/indices/managed/llama_cloud/base.py`
```
845
846
847
848
849
850
851
852
853
854
855
856
857
858
859
860
861
862
863
864
865
866
867
```
| ```
async def arefresh_ref_docs(
    self, documents: Sequence[Document], **update_kwargs: Any
) -> List[bool]:
"""Refresh an index with documents that have changed."""
    with self._callback_manager.as_trace("refresh"):
        upserted_documents = await self._aclient.pipelines.upsert_batch_pipeline_documents(
            pipeline_id=self.pipeline.id,
            request=[
                CloudDocumentCreate(
                    text=doc.text,
                    metadata=doc.metadata,
                    excluded_embed_metadata_keys=doc.excluded_embed_metadata_keys,
                    excluded_llm_metadata_keys=doc.excluded_llm_metadata_keys,
                    id=doc.id_,
                )
                for doc in documents
            ],
        )
        doc_ids = [doc.id for doc in upserted_documents]
        await self.await_for_completion(
            doc_ids=doc_ids, verbose=True, raise_on_error=True
        )
        return [True] * len(doc_ids)

```
  
---|---  
###  delete_ref_doc [#](https://developers.llamaindex.ai/python/framework-api-reference/indices/llama_cloud/#llama_index.indices.managed.llama_cloud.LlamaCloudIndex.delete_ref_doc "Permanent link")
```
delete_ref_doc(ref_doc_id: , delete_from_docstore:  = False, verbose:  = False, raise_if_not_found:  = False, **delete_kwargs: ) -> None

```

Delete a document and its nodes by using ref_doc_id.
Source code in `llama_index/indices/managed/llama_cloud/base.py`
```
869
870
871
872
873
874
875
876
877
878
879
880
881
882
883
884
885
886
887
888
889
890
891
```
| ```
def delete_ref_doc(
    self,
    ref_doc_id: str,
    delete_from_docstore: bool = False,
    verbose: bool = False,
    raise_if_not_found: bool = False,
    **delete_kwargs: Any,
) -> None:
"""Delete a document and its nodes by using ref_doc_id."""
    try:
        # we have to quote the ref_doc_id twice because it is used as a path parameter
        self._client.pipelines.delete_pipeline_document(
            pipeline_id=self.pipeline.id,
            document_id=quote_plus(quote_plus(ref_doc_id)),
        )
    except ApiError as e:
        if e.status_code == 404 and not raise_if_not_found:
            logger.warning(f"ref_doc_id {ref_doc_id} not found, nothing deleted.")
        else:
            raise

    # we have to wait for the pipeline instead of the document, because the document is already deleted
    self.wait_for_completion(verbose=verbose, raise_on_partial_success=False)

```
  
---|---  
###  adelete_ref_doc `async` [#](https://developers.llamaindex.ai/python/framework-api-reference/indices/llama_cloud/#llama_index.indices.managed.llama_cloud.LlamaCloudIndex.adelete_ref_doc "Permanent link")
```
adelete_ref_doc(ref_doc_id: , delete_from_docstore:  = False, verbose:  = False, raise_if_not_found:  = False, **delete_kwargs: ) -> None

```

Delete a document and its nodes by using ref_doc_id.
Source code in `llama_index/indices/managed/llama_cloud/base.py`
```
893
894
895
896
897
898
899
900
901
902
903
904
905
906
907
908
909
910
911
912
913
914
915
```
| ```
async def adelete_ref_doc(
    self,
    ref_doc_id: str,
    delete_from_docstore: bool = False,
    verbose: bool = False,
    raise_if_not_found: bool = False,
    **delete_kwargs: Any,
) -> None:
"""Delete a document and its nodes by using ref_doc_id."""
    try:
        # we have to quote the ref_doc_id twice because it is used as a path parameter
        await self._aclient.pipelines.delete_pipeline_document(
            pipeline_id=self.pipeline.id,
            document_id=quote_plus(quote_plus(ref_doc_id)),
        )
    except ApiError as e:
        if e.status_code == 404 and not raise_if_not_found:
            logger.warning(f"ref_doc_id {ref_doc_id} not found, nothing deleted.")
        else:
            raise

    # we have to wait for the pipeline instead of the document, because the document is already deleted
    await self.await_for_completion(verbose=verbose, raise_on_partial_success=False)

```
  
---|---  
###  upload_file [#](https://developers.llamaindex.ai/python/framework-api-reference/indices/llama_cloud/#llama_index.indices.managed.llama_cloud.LlamaCloudIndex.upload_file "Permanent link")
```
upload_file(file_path: , verbose:  = False, wait_for_ingestion:  = True, raise_on_error:  = False) -> 

```

Upload a file to the index.
Source code in `llama_index/indices/managed/llama_cloud/base.py`
```
917
918
919
920
921
922
923
924
925
926
927
928
929
930
931
932
933
934
935
936
937
938
939
940
941
942
```
| ```
def upload_file(
    self,
    file_path: str,
    verbose: bool = False,
    wait_for_ingestion: bool = True,
    raise_on_error: bool = False,
) -> str:
"""Upload a file to the index."""
    with open(file_path, "rb") as f:
        file = self._client.files.upload_file(
            project_id=self.project.id, upload_file=f
        )
        if verbose:
            print(f"Uploaded file {file.id} with name {file.name}")

    # Add file to pipeline
    pipeline_file_create = PipelineFileCreate(file_id=file.id)
    self._client.pipelines.add_files_to_pipeline_api(
        pipeline_id=self.pipeline.id, request=[pipeline_file_create]
    )

    if wait_for_ingestion:
        self.wait_for_completion(
            file_ids=[file.id], verbose=verbose, raise_on_error=raise_on_error
        )
    return file.id

```
  
---|---  
###  aupload_file `async` [#](https://developers.llamaindex.ai/python/framework-api-reference/indices/llama_cloud/#llama_index.indices.managed.llama_cloud.LlamaCloudIndex.aupload_file "Permanent link")
```
aupload_file(file_path: , verbose:  = False, wait_for_ingestion:  = True, raise_on_error:  = False) -> 

```

Upload a file to the index.
Source code in `llama_index/indices/managed/llama_cloud/base.py`
```
944
945
946
947
948
949
950
951
952
953
954
955
956
957
958
959
960
961
962
963
964
965
966
967
968
969
970
```
| ```
async def aupload_file(
    self,
    file_path: str,
    verbose: bool = False,
    wait_for_ingestion: bool = True,
    raise_on_error: bool = False,
) -> str:
"""Upload a file to the index."""
    with open(file_path, "rb") as f:
        file = await self._aclient.files.upload_file(
            project_id=self.project.id, upload_file=f
        )
        if verbose:
            print(f"Uploaded file {file.id} with name {file.name}")

    # Add file to pipeline
    pipeline_file_create = PipelineFileCreate(file_id=file.id)
    await self._aclient.pipelines.add_files_to_pipeline_api(
        pipeline_id=self.pipeline.id, request=[pipeline_file_create]
    )

    if wait_for_ingestion:
        await self.await_for_completion(
            file_ids=[file.id], verbose=verbose, raise_on_error=raise_on_error
        )

    return file.id

```
  
---|---  
###  upload_file_from_url [#](https://developers.llamaindex.ai/python/framework-api-reference/indices/llama_cloud/#llama_index.indices.managed.llama_cloud.LlamaCloudIndex.upload_file_from_url "Permanent link")
```
upload_file_from_url(file_name: , url: , proxy_url: Optional[] = None, request_headers: Optional[[, ]] = None, verify_ssl:  = True, follow_redirects:  = True, verbose:  = False, wait_for_ingestion:  = True, raise_on_error:  = False) -> 

```

Upload a file from a URL to the index.
Source code in `llama_index/indices/managed/llama_cloud/base.py`
```
 972
 973
 974
 975
 976
 977
 978
 979
 980
 981
 982
 983
 984
 985
 986
 987
 988
 989
 990
 991
 992
 993
 994
 995
 996
 997
 998
 999
1000
1001
1002
1003
1004
1005
1006
1007
```
| ```
def upload_file_from_url(
    self,
    file_name: str,
    url: str,
    proxy_url: Optional[str] = None,
    request_headers: Optional[Dict[str, str]] = None,
    verify_ssl: bool = True,
    follow_redirects: bool = True,
    verbose: bool = False,
    wait_for_ingestion: bool = True,
    raise_on_error: bool = False,
) -> str:
"""Upload a file from a URL to the index."""
    file = self._client.files.upload_file_from_url(
        project_id=self.project.id,
        name=file_name,
        url=url,
        proxy_url=proxy_url,
        request_headers=request_headers,
        verify_ssl=verify_ssl,
        follow_redirects=follow_redirects,
    )
    if verbose:
        print(f"Uploaded file {file.id} with ID {file.id}")

    # Add file to pipeline
    pipeline_file_create = PipelineFileCreate(file_id=file.id)
    self._client.pipelines.add_files_to_pipeline_api(
        pipeline_id=self.pipeline.id, request=[pipeline_file_create]
    )

    if wait_for_ingestion:
        self.wait_for_completion(
            file_ids=[file.id], verbose=verbose, raise_on_error=raise_on_error
        )
    return file.id

```
  
---|---  
###  aupload_file_from_url `async` [#](https://developers.llamaindex.ai/python/framework-api-reference/indices/llama_cloud/#llama_index.indices.managed.llama_cloud.LlamaCloudIndex.aupload_file_from_url "Permanent link")
```
aupload_file_from_url(file_name: , url: , proxy_url: Optional[] = None, request_headers: Optional[[, ]] = None, verify_ssl:  = True, follow_redirects:  = True, verbose:  = False, wait_for_ingestion:  = True, raise_on_error:  = False) -> 

```

Upload a file from a URL to the index.
Source code in `llama_index/indices/managed/llama_cloud/base.py`
```
1009
1010
1011
1012
1013
1014
1015
1016
1017
1018
1019
1020
1021
1022
1023
1024
1025
1026
1027
1028
1029
1030
1031
1032
1033
1034
1035
1036
1037
1038
1039
1040
1041
1042
1043
1044
1045
```
| ```
async def aupload_file_from_url(
    self,
    file_name: str,
    url: str,
    proxy_url: Optional[str] = None,
    request_headers: Optional[Dict[str, str]] = None,
    verify_ssl: bool = True,
    follow_redirects: bool = True,
    verbose: bool = False,
    wait_for_ingestion: bool = True,
    raise_on_error: bool = False,
) -> str:
"""Upload a file from a URL to the index."""
    file = await self._aclient.files.upload_file_from_url(
        project_id=self.project.id,
        name=file_name,
        url=url,
        proxy_url=proxy_url,
        request_headers=request_headers,
        verify_ssl=verify_ssl,
        follow_redirects=follow_redirects,
    )
    if verbose:
        print(f"Uploaded file {file.id} with ID {file.id}")

    # Add file to pipeline
    pipeline_file_create = PipelineFileCreate(file_id=file.id)
    await self._aclient.pipelines.add_files_to_pipeline_api(
        pipeline_id=self.pipeline.id, request=[pipeline_file_create]
    )

    if wait_for_ingestion:
        await self.await_for_completion(
            file_ids=[file.id], verbose=verbose, raise_on_error=raise_on_error
        )

    return file.id

```
  
---|---  
###  build_index_from_nodes [#](https://developers.llamaindex.ai/python/framework-api-reference/indices/llama_cloud/#llama_index.indices.managed.llama_cloud.LlamaCloudIndex.build_index_from_nodes "Permanent link")
```
build_index_from_nodes(nodes: Sequence[]) -> None

```

Build the index from nodes.
Source code in `llama_index/indices/managed/llama_cloud/base.py`
```
1053
1054
1055
1056
1057
```
| ```
def build_index_from_nodes(self, nodes: Sequence[BaseNode]) -> None:
"""Build the index from nodes."""
    raise NotImplementedError(
        "build_index_from_nodes not implemented for LlamaCloudIndex."
    )

```
  
---|---  
###  insert_nodes [#](https://developers.llamaindex.ai/python/framework-api-reference/indices/llama_cloud/#llama_index.indices.managed.llama_cloud.LlamaCloudIndex.insert_nodes "Permanent link")
```
insert_nodes(nodes: Sequence[], **insert_kwargs: ) -> None

```

Insert a set of nodes.
Source code in `llama_index/indices/managed/llama_cloud/base.py`
```
1059
1060
1061
```
| ```
def insert_nodes(self, nodes: Sequence[BaseNode], **insert_kwargs: Any) -> None:
"""Insert a set of nodes."""
    raise NotImplementedError("insert_nodes not implemented for LlamaCloudIndex.")

```
  
---|---  
###  delete_nodes [#](https://developers.llamaindex.ai/python/framework-api-reference/indices/llama_cloud/#llama_index.indices.managed.llama_cloud.LlamaCloudIndex.delete_nodes "Permanent link")
```
delete_nodes(node_ids: [], delete_from_docstore:  = False, **delete_kwargs: ) -> None

```

Delete a set of nodes.
Source code in `llama_index/indices/managed/llama_cloud/base.py`
```
1063
1064
1065
1066
1067
1068
1069
1070
```
| ```
def delete_nodes(
    self,
    node_ids: List[str],
    delete_from_docstore: bool = False,
    **delete_kwargs: Any,
) -> None:
"""Delete a set of nodes."""
    raise NotImplementedError("delete_nodes not implemented for LlamaCloudIndex.")

```
  
---|---  
##  LlamaCloudRetriever [#](https://developers.llamaindex.ai/python/framework-api-reference/indices/llama_cloud/#llama_index.indices.managed.llama_cloud.LlamaCloudRetriever "Permanent link")
Bases: 
Source code in `llama_index/indices/managed/llama_cloud/retriever.py`
```
 30
 31
 32
 33
 34
 35
 36
 37
 38
 39
 40
 41
 42
 43
 44
 45
 46
 47
 48
 49
 50
 51
 52
 53
 54
 55
 56
 57
 58
 59
 60
 61
 62
 63
 64
 65
 66
 67
 68
 69
 70
 71
 72
 73
 74
 75
 76
 77
 78
 79
 80
 81
 82
 83
 84
 85
 86
 87
 88
 89
 90
 91
 92
 93
 94
 95
 96
 97
 98
 99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
```
| ```
@deprecated(
    reason=DEPRECATION_REASON,
    version="0.9.1",
)
class LlamaCloudRetriever(BaseRetriever):
    def __init__(
        self,
        # index identifier
        name: Optional[str] = None,
        index_id: Optional[str] = None,  # alias for pipeline_id
        id: Optional[str] = None,  # alias for pipeline_id
        pipeline_id: Optional[str] = None,
        # project identifier
        project_name: Optional[str] = DEFAULT_PROJECT_NAME,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        # connection params
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        app_url: Optional[str] = None,
        timeout: int = 60,
        httpx_client: Optional[httpx.Client] = None,
        async_httpx_client: Optional[httpx.AsyncClient] = None,
        # retrieval params
        dense_similarity_top_k: Optional[int] = None,
        sparse_similarity_top_k: Optional[int] = None,
        enable_reranking: Optional[bool] = None,
        rerank_top_n: Optional[int] = None,
        alpha: Optional[float] = None,
        filters: Optional[MetadataFilters] = None,
        retrieval_mode: Optional[str] = None,
        files_top_k: Optional[int] = None,
        retrieve_image_nodes: Optional[bool] = None,
        retrieve_page_screenshot_nodes: Optional[bool] = None,
        retrieve_page_figure_nodes: Optional[bool] = None,
        search_filters_inference_schema: Optional[BaseModel] = None,
        **kwargs: Any,
    ) -> None:
"""Initialize the Platform Retriever."""
        if sum([bool(id), bool(index_id), bool(pipeline_id), bool(name)]) != 1:
            raise ValueError(
                "Exactly one of `name`, `id`, `pipeline_id` or `index_id` must be provided to identify the index."
            )

        # initialize clients
        self._httpx_client = httpx_client
        self._async_httpx_client = async_httpx_client
        self._client = get_client(api_key, base_url, app_url, timeout, httpx_client)
        self._aclient = get_aclient(
            api_key, base_url, app_url, timeout, async_httpx_client
        )

        pipeline_id = id or index_id or pipeline_id
        self.project, self.pipeline = resolve_project_and_pipeline(
            self._client, name, pipeline_id, project_name, project_id, organization_id
        )
        self.name = self.pipeline.name
        self.project_name = self.project.name

        # retrieval params
        self._dense_similarity_top_k = (
            dense_similarity_top_k if dense_similarity_top_k is not None else OMIT
        )
        self._sparse_similarity_top_k = (
            sparse_similarity_top_k if sparse_similarity_top_k is not None else OMIT
        )
        self._enable_reranking = (
            enable_reranking if enable_reranking is not None else OMIT
        )
        self._rerank_top_n = rerank_top_n if rerank_top_n is not None else OMIT
        self._alpha = alpha if alpha is not None else OMIT
        self._filters = filters if filters is not None else OMIT
        self._retrieval_mode = retrieval_mode if retrieval_mode is not None else OMIT
        self._files_top_k = files_top_k if files_top_k is not None else OMIT
        if retrieve_image_nodes is not None:
            logger.warning(
                "The `retrieve_image_nodes` parameter is deprecated. "
                "Use `retrieve_page_screenshot_nodes` and `retrieve_page_figure_nodes` instead."
            )
        if retrieve_image_nodes:
            if (
                retrieve_page_screenshot_nodes is False
                or retrieve_page_figure_nodes is False
            ):
                raise ValueError(
                    "If `retrieve_image_nodes` is set to True, "
                    "both `retrieve_page_screenshot_nodes` and `retrieve_page_figure_nodes` must also be set to True or omitted."
                )
            retrieve_page_screenshot_nodes = True
            retrieve_page_figure_nodes = True
        self._retrieve_page_screenshot_nodes = (
            retrieve_page_screenshot_nodes
            if retrieve_page_screenshot_nodes is not None
            else OMIT
        )
        self._retrieve_page_figure_nodes = (
            retrieve_page_figure_nodes
            if retrieve_page_figure_nodes is not None
            else OMIT
        )
        self._search_filters_inference_schema = search_filters_inference_schema

        super().__init__(
            callback_manager=kwargs.get("callback_manager"),
            verbose=kwargs.get("verbose", False),
        )

    def _result_nodes_to_node_with_score(
        self, result_nodes: List[TextNodeWithScore]
    ) -> List[NodeWithScore]:
        nodes = []
        for res in result_nodes:
            text_node = TextNode.parse_obj(res.node.dict())
            nodes.append(NodeWithScore(node=text_node, score=res.score))

        return nodes

    def _retrieve(self, query_bundle: QueryBundle) -> List[NodeWithScore]:
"""Retrieve from the platform."""
        search_filters_inference_schema = OMIT
        if self._search_filters_inference_schema is not None:
            search_filters_inference_schema = (
                self._search_filters_inference_schema.model_json_schema()
            )
        results = self._client.pipelines.run_search(
            query=query_bundle.query_str,
            pipeline_id=self.pipeline.id,
            dense_similarity_top_k=self._dense_similarity_top_k,
            sparse_similarity_top_k=self._sparse_similarity_top_k,
            enable_reranking=self._enable_reranking,
            rerank_top_n=self._rerank_top_n,
            alpha=self._alpha,
            search_filters=self._filters,
            files_top_k=self._files_top_k,
            retrieval_mode=self._retrieval_mode,
            retrieve_page_screenshot_nodes=self._retrieve_page_screenshot_nodes,
            retrieve_page_figure_nodes=self._retrieve_page_figure_nodes,
            search_filters_inference_schema=search_filters_inference_schema,
        )

        result_nodes = self._result_nodes_to_node_with_score(results.retrieval_nodes)
        if self._retrieve_page_screenshot_nodes:
            result_nodes.extend(
                page_screenshot_nodes_to_node_with_score(
                    self._client, results.image_nodes, self.project.id
                )
            )
        if self._retrieve_page_figure_nodes:
            result_nodes.extend(
                page_figure_nodes_to_node_with_score(
                    self._client, results.page_figure_nodes, self.project.id
                )
            )

        return result_nodes

    async def _aretrieve(self, query_bundle: QueryBundle) -> List[NodeWithScore]:
"""Asynchronously retrieve from the platform."""
        search_filters_inference_schema = OMIT
        if self._search_filters_inference_schema is not None:
            search_filters_inference_schema = (
                self._search_filters_inference_schema.model_json_schema()
            )
        results = await self._aclient.pipelines.run_search(
            query=query_bundle.query_str,
            pipeline_id=self.pipeline.id,
            dense_similarity_top_k=self._dense_similarity_top_k,
            sparse_similarity_top_k=self._sparse_similarity_top_k,
            enable_reranking=self._enable_reranking,
            rerank_top_n=self._rerank_top_n,
            alpha=self._alpha,
            search_filters=self._filters,
            files_top_k=self._files_top_k,
            retrieval_mode=self._retrieval_mode,
            retrieve_page_screenshot_nodes=self._retrieve_page_screenshot_nodes,
            retrieve_page_figure_nodes=self._retrieve_page_figure_nodes,
            search_filters_inference_schema=search_filters_inference_schema,
        )

        result_nodes = self._result_nodes_to_node_with_score(results.retrieval_nodes)
        if self._retrieve_page_screenshot_nodes:
            result_nodes.extend(
                await apage_screenshot_nodes_to_node_with_score(
                    self._aclient, results.image_nodes, self.project.id
                )
            )
        if self._retrieve_page_figure_nodes:
            result_nodes.extend(
                await apage_figure_nodes_to_node_with_score(
                    self._aclient, results.page_figure_nodes, self.project.id
                )
            )

        return result_nodes

```
  
---|---  
##  LlamaCloudCompositeRetriever [#](https://developers.llamaindex.ai/python/framework-api-reference/indices/llama_cloud/#llama_index.indices.managed.llama_cloud.LlamaCloudCompositeRetriever "Permanent link")
Bases: 
Source code in `llama_index/indices/managed/llama_cloud/composite_retriever.py`
```
 29
 30
 31
 32
 33
 34
 35
 36
 37
 38
 39
 40
 41
 42
 43
 44
 45
 46
 47
 48
 49
 50
 51
 52
 53
 54
 55
 56
 57
 58
 59
 60
 61
 62
 63
 64
 65
 66
 67
 68
 69
 70
 71
 72
 73
 74
 75
 76
 77
 78
 79
 80
 81
 82
 83
 84
 85
 86
 87
 88
 89
 90
 91
 92
 93
 94
 95
 96
 97
 98
 99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
255
256
257
258
259
260
261
262
263
264
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
285
286
287
288
289
290
291
292
293
294
295
296
297
298
299
300
301
302
303
304
305
306
307
308
309
```
| ```
@deprecated(
    reason=DEPRECATION_REASON,
    version="0.9.1",
)
class LlamaCloudCompositeRetriever(BaseRetriever):
    def __init__(
        self,
        # retriever identifier
        name: Optional[str] = None,
        retriever_id: Optional[str] = None,
        # project identifier
        project_name: Optional[str] = DEFAULT_PROJECT_NAME,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        # creation options
        create_if_not_exists: bool = False,
        # connection params
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        app_url: Optional[str] = None,
        timeout: int = 60,
        httpx_client: Optional[httpx.Client] = None,
        async_httpx_client: Optional[httpx.AsyncClient] = None,
        # composite retrieval params
        mode: Optional[CompositeRetrievalMode] = None,
        rerank_top_n: Optional[int] = None,
        rerank_config: Optional[ReRankConfig] = None,
        persisted: Optional[bool] = True,
        **kwargs: Any,
    ) -> None:
"""Initialize the Composite Retriever."""
        # initialize clients
        self._client = get_client(api_key, base_url, app_url, timeout, httpx_client)
        self._aclient = get_aclient(
            api_key, base_url, app_url, timeout, async_httpx_client
        )

        self.project = resolve_project(
            self._client, project_name, project_id, organization_id
        )

        self.name = name
        self.project_name = self.project.name
        self._persisted = persisted

        self.retriever = resolve_retriever(
            self._client, self.project, name, retriever_id, persisted
        )

        if self.retriever is None and persisted:
            if create_if_not_exists:
                self.retriever = self._client.retrievers.upsert_retriever(
                    project_id=self.project.id,
                    request=RetrieverCreate(name=self.name, pipelines=[]),
                )
            else:
                raise ValueError(
                    f"Retriever with name '{self.name}' does not exist in project."
                )

        # composite retrieval params
        self._mode = mode if mode is not None else OMIT
        self._rerank_top_n = rerank_top_n if rerank_top_n is not None else OMIT
        self._rerank_config = rerank_config if rerank_config is not None else OMIT

        super().__init__(
            callback_manager=kwargs.get("callback_manager"),
            verbose=kwargs.get("verbose", False),
        )

    @property
    def retriever_pipelines(self) -> List[RetrieverPipeline]:
        return self.retriever.pipelines or []

    def update_retriever_pipelines(
        self, pipelines: List[RetrieverPipeline]
    ) -> Retriever:
        if self._persisted:
            self.retriever = self._client.retrievers.update_retriever(
                self.retriever.id, pipelines=pipelines
            )
        else:
            # Update in-memory retriever for non-persisted case using copy
            self.retriever = self.retriever.copy(update={"pipelines": pipelines})
        return self.retriever

    def add_index(
        self,
        index: LlamaCloudIndex,
        name: Optional[str] = None,
        description: Optional[str] = None,
        preset_retrieval_parameters: Optional[PresetRetrievalParams] = None,
    ) -> Retriever:
        name = name or index.name
        preset_retrieval_parameters = (
            preset_retrieval_parameters or index.pipeline.preset_retrieval_parameters
        )
        retriever_pipeline = RetrieverPipeline(
            pipeline_id=index.id,
            name=name,
            description=description,
            preset_retrieval_parameters=preset_retrieval_parameters,
        )
        current_retriever_pipelines_by_name = {
            pipeline.name: pipeline for pipeline in (self.retriever_pipelines or [])
        }
        current_retriever_pipelines_by_name[retriever_pipeline.name] = (
            retriever_pipeline
        )
        return self.update_retriever_pipelines(
            list(current_retriever_pipelines_by_name.values())
        )

    def remove_index(self, name: str) -> bool:
        current_retriever_pipeline_names = self.retriever.pipelines or []
        new_retriever_pipelines = [
            pipeline
            for pipeline in current_retriever_pipeline_names
            if pipeline.name != name
        ]
        if len(new_retriever_pipelines) == len(current_retriever_pipeline_names):
            return False
        self.update_retriever_pipelines(new_retriever_pipelines)
        return True

    async def aupdate_retriever_pipelines(
        self, pipelines: List[RetrieverPipeline]
    ) -> Retriever:
        if self._persisted:
            self.retriever = await self._aclient.retrievers.update_retriever(
                self.retriever.id, pipelines=pipelines
            )
        else:
            # Update in-memory retriever for non-persisted case using copy
            self.retriever = self.retriever.copy(update={"pipelines": pipelines})
        return self.retriever

    async def async_add_index(
        self,
        index: LlamaCloudIndex,
        name: Optional[str] = None,
        description: Optional[str] = None,
        preset_retrieval_parameters: Optional[PresetRetrievalParams] = None,
    ) -> Retriever:
        name = name or index.name
        preset_retrieval_parameters = (
            preset_retrieval_parameters or index.pipeline.preset_retrieval_parameters
        )
        retriever_pipeline = RetrieverPipeline(
            pipeline_id=index.id,
            name=name,
            description=description,
            preset_retrieval_parameters=preset_retrieval_parameters,
        )
        current_retriever_pipelines_by_name = {
            pipeline.name: pipeline for pipeline in (self.retriever_pipelines or [])
        }
        current_retriever_pipelines_by_name[retriever_pipeline.name] = (
            retriever_pipeline
        )
        return await self.aupdate_retriever_pipelines(
            list(current_retriever_pipelines_by_name.values())
        )

    async def aremove_index(self, name: str) -> bool:
        current_retriever_pipeline_names = self.retriever.pipelines or []
        new_retriever_pipelines = [
            pipeline
            for pipeline in current_retriever_pipeline_names
            if pipeline.name != name
        ]
        if len(new_retriever_pipelines) == len(current_retriever_pipeline_names):
            return False
        await self.aupdate_retriever_pipelines(new_retriever_pipelines)
        return True

    def _result_nodes_to_node_with_score(
        self, composite_retrieval_node: CompositeRetrievedTextNodeWithScore
    ) -> NodeWithScore:
        return NodeWithScore(
            node=TextNode(
                id=composite_retrieval_node.node.id,
                text=composite_retrieval_node.node.text,
                metadata=composite_retrieval_node.node.metadata,
            ),
            score=composite_retrieval_node.score,
        )

    def _retrieve(
        self,
        query_bundle: QueryBundle,
        mode: Optional[CompositeRetrievalMode] = None,
        rerank_top_n: Optional[int] = None,
        rerank_config: Optional[ReRankConfig] = None,
    ) -> List[NodeWithScore]:
        mode = mode if mode is not None else self._mode

        rerank_top_n = rerank_top_n if rerank_top_n is not None else self._rerank_top_n
        rerank_config = (
            rerank_config if rerank_config is not None else self._rerank_config
        )

        # Inject rerank_top_n into rerank_config if specified
        if rerank_top_n is not None and rerank_top_n != OMIT:
            if rerank_config is None or rerank_config == OMIT:
                rerank_config = ReRankConfig(top_n=rerank_top_n)
            else:
                # Update existing rerank_config with top_n
                rerank_config = rerank_config.copy(update={"top_n": rerank_top_n})

        if self._persisted:
            result = self._client.retrievers.retrieve(
                self.retriever.id,
                mode=mode,
                rerank_config=rerank_config,
                query=query_bundle.query_str,
            )
        else:
            result = self._client.retrievers.direct_retrieve(
                project_id=self.project.id,
                mode=mode,
                rerank_config=rerank_config,
                query=query_bundle.query_str,
                pipelines=self.retriever.pipelines,
            )
        node_w_scores = [
            self._result_nodes_to_node_with_score(node) for node in result.nodes
        ]
        image_nodes_w_scores = page_screenshot_nodes_to_node_with_score(
            self._client, result.image_nodes, self.retriever.project_id
        )
        return sorted(
            node_w_scores + image_nodes_w_scores, key=lambda x: x.score, reverse=True
        )

    async def _aretrieve(
        self,
        query_bundle: QueryBundle,
        mode: Optional[CompositeRetrievalMode] = None,
        rerank_top_n: Optional[int] = None,
        rerank_config: Optional[ReRankConfig] = None,
    ) -> List[NodeWithScore]:
        mode = mode if mode is not None else self._mode

        rerank_top_n = rerank_top_n if rerank_top_n is not None else self._rerank_top_n
        rerank_config = (
            rerank_config if rerank_config is not None else self._rerank_config
        )

        # Inject rerank_top_n into rerank_config if specified
        if rerank_top_n is not None and rerank_top_n != OMIT:
            if rerank_config is None or rerank_config == OMIT:
                rerank_config = ReRankConfig(top_n=rerank_top_n)
            else:
                # Update existing rerank_config with top_n
                rerank_config = rerank_config.copy(update={"top_n": rerank_top_n})

        if self._persisted:
            result = await self._aclient.retrievers.retrieve(
                self.retriever.id,
                mode=mode,
                rerank_config=rerank_config,
                query=query_bundle.query_str,
            )
        else:
            result = await self._aclient.retrievers.direct_retrieve(
                project_id=self.project.id,
                mode=mode,
                rerank_config=rerank_config,
                query=query_bundle.query_str,
                pipelines=self.retriever.pipelines,
            )
        node_w_scores = [
            self._result_nodes_to_node_with_score(node) for node in result.nodes
        ]
        image_nodes_w_scores = page_screenshot_nodes_to_node_with_score(
            self._aclient, result.image_nodes, self.retriever.project_id
        )
        return sorted(
            node_w_scores + image_nodes_w_scores, key=lambda x: x.score, reverse=True
        )

```
  
---|---  
options: members: - LlamaCloudIndex
