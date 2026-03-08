# Aws bedrock agentcore
AWS Bedrock AgentCore tools.
##  AgentCoreBrowserToolSpec [#](https://developers.llamaindex.ai/python/framework-api-reference/tools/aws_bedrock_agentcore/#llama_index.tools.aws_bedrock_agentcore.AgentCoreBrowserToolSpec "Permanent link")
Bases: 
AWS Bedrock AgentCore Browser Tool Spec.
This toolkit provides a set of tools for working with a remote browser environment:
  * navigate_browser - Navigate to a URL
  * click_element - Click on an element using CSS selectors
  * extract_text - Extract all text from the current webpage
  * extract_hyperlinks - Extract all hyperlinks from the current webpage
  * get_elements - Get elements matching a CSS selector
  * navigate_back - Navigate to the previous page
  * current_webpage - Get information about the current webpage


The toolkit supports multiple threads by maintaining separate browser sessions for each thread ID.
Source code in `llama_index/tools/aws_bedrock_agentcore/browser/base.py`
```
 25
 26
 27
 28
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
```
| ```
class AgentCoreBrowserToolSpec(BaseToolSpec):
"""
    AWS Bedrock AgentCore Browser Tool Spec.

    This toolkit provides a set of tools for working with a remote browser environment:

    * navigate_browser - Navigate to a URL
    * click_element - Click on an element using CSS selectors
    * extract_text - Extract all text from the current webpage
    * extract_hyperlinks - Extract all hyperlinks from the current webpage
    * get_elements - Get elements matching a CSS selector
    * navigate_back - Navigate to the previous page
    * current_webpage - Get information about the current webpage

    The toolkit supports multiple threads by maintaining separate browser sessions for each thread ID.
    """

    spec_functions = [
        ("navigate_browser", "anavigate_browser"),
        ("click_element", "aclick_element"),
        ("extract_text", "aextract_text"),
        ("extract_hyperlinks", "aextract_hyperlinks"),
        ("get_elements", "aget_elements"),
        ("navigate_back", "anavigate_back"),
        ("current_webpage", "acurrent_webpage"),
    ]

    def __init__(self, region: Optional[str] = None) -> None:
"""
        Initialize the AWS Bedrock AgentCore Browser Tool Spec.

        Args:
            region (Optional[str]): AWS region to use for Bedrock AgentCore services.
                If not provided, will try to get it from environment variables.

        """
        self.region = region if region is not None else get_aws_region()
        self._browser_clients: Dict[str, BrowserClient] = {}
        self._session_manager = BrowserSessionManager(region=self.region)

    def _get_or_create_browser_client(
        self, thread_id: str = "default"
    ) -> BrowserClient:
"""
        Get or create a browser client for the specified thread.

        Args:
            thread_id: Thread ID for the browser session

        Returns:
            BrowserClient instance

        """
        if thread_id in self._browser_clients:
            return self._browser_clients[thread_id]

        # Create a new browser client for this thread
        browser_client = BrowserClient(self.region)
        self._browser_clients[thread_id] = browser_client
        return browser_client

    def navigate_browser(
        self,
        url: str,
        thread_id: str = "default",
    ) -> str:
"""
        Navigate to a URL (synchronous version).

        Args:
            url (str): URL to navigate to.
            thread_id (str): Thread ID for the browser session.

        Returns:
            str: Confirmation message.

        """
        try:
            # Validate URL scheme
            parsed_url = urlparse(url)
            if parsed_url.scheme not in ("http", "https"):
                return f"URL scheme must be 'http' or 'https', got: {parsed_url.scheme}"

            # Get browser and navigate to URL
            browser = self._session_manager.get_sync_browser(thread_id)
            page = get_current_page(browser)
            response = page.goto(url)
            status = response.status if response else "unknown"

            # Release the browser
            self._session_manager.release_sync_browser(thread_id)

            return f"Navigated to {url} with status code {status}"
        except Exception as e:
            return f"Error navigating to URL: {e!s}"

    async def anavigate_browser(
        self,
        url: str,
        thread_id: str = "default",
    ) -> str:
"""
        Navigate to a URL (asynchronous version).

        Args:
            url (str): URL to navigate to.
            thread_id (str): Thread ID for the browser session.

        Returns:
            str: Confirmation message.

        """
        try:
            # Validate URL scheme
            parsed_url = urlparse(url)
            if parsed_url.scheme not in ("http", "https"):
                return f"URL scheme must be 'http' or 'https', got: {parsed_url.scheme}"

            # Get browser and navigate to URL
            browser = await self._session_manager.get_async_browser(thread_id)
            page = await aget_current_page(browser)
            response = await page.goto(url)
            status = response.status if response else "unknown"

            # Release the browser
            await self._session_manager.release_async_browser(thread_id)

            return f"Navigated to {url} with status code {status}"
        except Exception as e:
            return f"Error navigating to URL: {e!s}"

    def click_element(
        self,
        selector: str,
        thread_id: str = "default",
    ) -> str:
"""
        Click on an element with the given CSS selector (synchronous version).

        Args:
            selector (str): CSS selector for the element to click on.
            thread_id (str): Thread ID for the browser session.

        Returns:
            str: Confirmation message.

        """
        try:
            # Get browser and click on element
            browser = self._session_manager.get_sync_browser(thread_id)
            page = get_current_page(browser)

            try:
                page.click(selector, timeout=5000)
                result = f"Clicked on element with selector '{selector}'"
            except Exception as click_error:
                result = f"Unable to click on element with selector '{selector}': {click_error!s}"

            # Release the browser
            self._session_manager.release_sync_browser(thread_id)

            return result
        except Exception as e:
            return f"Error clicking on element: {e!s}"

    async def aclick_element(
        self,
        selector: str,
        thread_id: str = "default",
    ) -> str:
"""
        Click on an element with the given CSS selector (asynchronous version).

        Args:
            selector (str): CSS selector for the element to click on.
            thread_id (str): Thread ID for the browser session.

        Returns:
            str: Confirmation message.

        """
        try:
            # Get browser and click on element
            browser = await self._session_manager.get_async_browser(thread_id)
            page = await aget_current_page(browser)

            try:
                await page.click(selector, timeout=5000)
                result = f"Clicked on element with selector '{selector}'"
            except Exception as click_error:
                result = f"Unable to click on element with selector '{selector}': {click_error!s}"

            # Release the browser
            await self._session_manager.release_async_browser(thread_id)

            return result
        except Exception as e:
            return f"Error clicking on element: {e!s}"

    def extract_text(
        self,
        selector: Optional[str] = None,
        thread_id: str = "default",
    ) -> str:
"""
        Extract text from the current page (synchronous version).

        Args:
            selector (Optional[str]): CSS selector for the element to extract text from. If not provided, extracts text from the entire page.
            thread_id (str): Thread ID for the browser session.

        Returns:
            str: The extracted text.

        """
        try:
            # Get browser and extract text
            browser = self._session_manager.get_sync_browser(thread_id)
            page = get_current_page(browser)

            if selector:
                try:
                    element = page.query_selector(selector)
                    if element:
                        text = element.text_content()
                        result = text if text else "Element found but contains no text"
                    else:
                        result = f"No element found with selector '{selector}'"
                except Exception as selector_error:
                    result = f"Error extracting text from selector '{selector}': {selector_error!s}"
            else:
                # Extract text from the entire page
                result = page.content()

            # Release the browser
            self._session_manager.release_sync_browser(thread_id)

            return result
        except Exception as e:
            return f"Error extracting text: {e!s}"

    async def aextract_text(
        self,
        selector: Optional[str] = None,
        thread_id: str = "default",
    ) -> str:
"""
        Extract text from the current page (asynchronous version).

        Args:
            selector (Optional[str]): CSS selector for the element to extract text from. If not provided, extracts text from the entire page.
            thread_id (str): Thread ID for the browser session.

        Returns:
            str: The extracted text.

        """
        try:
            # Get browser and extract text
            browser = await self._session_manager.get_async_browser(thread_id)
            page = await aget_current_page(browser)

            if selector:
                try:
                    element = await page.query_selector(selector)
                    if element:
                        text = await element.text_content()
                        result = text if text else "Element found but contains no text"
                    else:
                        result = f"No element found with selector '{selector}'"
                except Exception as selector_error:
                    result = f"Error extracting text from selector '{selector}': {selector_error!s}"
            else:
                # Extract text from the entire page
                result = await page.content()

            # Release the browser
            await self._session_manager.release_async_browser(thread_id)

            return result
        except Exception as e:
            return f"Error extracting text: {e!s}"

    def extract_hyperlinks(
        self,
        thread_id: str = "default",
    ) -> str:
"""
        Extract hyperlinks from the current page (synchronous version).

        Args:
            thread_id (str): Thread ID for the browser session.

        Returns:
            str: The extracted hyperlinks.

        """
        try:
            # Get browser and extract hyperlinks
            browser = self._session_manager.get_sync_browser(thread_id)
            page = get_current_page(browser)

            # Extract all hyperlinks from the page
            links = page.eval_on_selector_all(
                "a[href]",
"""
                (elements) => {
                    return elements.map(el => {
                        return {
                            text: el.innerText || el.textContent,
                            href: el.href



,
            )

            # Format the links
            formatted_links = []
            for i, link in enumerate(links):
                formatted_links.append(
                    f"{i+1}. {link.get('text','No text')}: {link.get('href','No href')}"
                )

            result = (
                "\n".join(formatted_links)
                if formatted_links
                else "No hyperlinks found on the page"
            )

            # Release the browser
            self._session_manager.release_sync_browser(thread_id)

            return result
        except Exception as e:
            return f"Error extracting hyperlinks: {e!s}"

    async def aextract_hyperlinks(
        self,
        thread_id: str = "default",
    ) -> str:
"""
        Extract hyperlinks from the current page (asynchronous version).

        Args:
            thread_id (str): Thread ID for the browser session.

        Returns:
            str: The extracted hyperlinks.

        """
        try:
            # Get browser and extract hyperlinks
            browser = await self._session_manager.get_async_browser(thread_id)
            page = await aget_current_page(browser)

            # Extract all hyperlinks from the page
            links = await page.eval_on_selector_all(
                "a[href]",
"""
                (elements) => {
                    return elements.map(el => {
                        return {
                            text: el.innerText || el.textContent,
                            href: el.href



,
            )

            # Format the links
            formatted_links = []
            for i, link in enumerate(links):
                formatted_links.append(
                    f"{i+1}. {link.get('text','No text')}: {link.get('href','No href')}"
                )

            result = (
                "\n".join(formatted_links)
                if formatted_links
                else "No hyperlinks found on the page"
            )

            # Release the browser
            await self._session_manager.release_async_browser(thread_id)

            return result
        except Exception as e:
            return f"Error extracting hyperlinks: {e!s}"

    def get_elements(
        self,
        selector: str,
        thread_id: str = "default",
    ) -> str:
"""
        Get elements matching a CSS selector (synchronous version).

        Args:
            selector (str): CSS selector for the elements to get.
            thread_id (str): Thread ID for the browser session.

        Returns:
            str: Information about the matching elements.

        """
        try:
            # Get browser and find elements
            browser = self._session_manager.get_sync_browser(thread_id)
            page = get_current_page(browser)

            # Find elements matching the selector
            elements = page.query_selector_all(selector)

            if not elements:
                result = f"No elements found matching selector '{selector}'"
            else:
                # Extract information about the elements
                elements_info = []
                for i, element in enumerate(elements):
                    tag_name = element.evaluate("el => el.tagName.toLowerCase()")
                    text = element.text_content() or ""
                    attributes = element.evaluate("""
                        (el) => {
                            const attrs = {};
                            for (const attr of el.attributes) {
                                attrs[attr.name] = attr.value;

                            return attrs;

)

                    # Format element info
                    attr_str = ", ".join([f'{k}="{v}"' for k, v in attributes.items()])
                    elements_info.append(
                        f"{i+1}. <{tag_name}{attr_str}{text}</{tag_name}>"
                    )

                result = (
                    f"Found {len(elements)} element(s) matching selector '{selector}':\n"
                    + "\n".join(elements_info)
                )

            # Release the browser
            self._session_manager.release_sync_browser(thread_id)

            return result
        except Exception as e:
            return f"Error getting elements: {e!s}"

    async def aget_elements(
        self,
        selector: str,
        thread_id: str = "default",
    ) -> str:
"""
        Get elements matching a CSS selector (asynchronous version).

        Args:
            selector (str): CSS selector for the elements to get.
            thread_id (str): Thread ID for the browser session.

        Returns:
            str: Information about the matching elements.

        """
        try:
            # Get browser and find elements
            browser = await self._session_manager.get_async_browser(thread_id)
            page = await aget_current_page(browser)

            # Find elements matching the selector
            elements = await page.query_selector_all(selector)

            if not elements:
                result = f"No elements found matching selector '{selector}'"
            else:
                # Extract information about the elements
                elements_info = []
                for i, element in enumerate(elements):
                    tag_name = await element.evaluate("el => el.tagName.toLowerCase()")
                    text = await element.text_content() or ""
                    attributes = await element.evaluate("""
                        (el) => {
                            const attrs = {};
                            for (const attr of el.attributes) {
                                attrs[attr.name] = attr.value;

                            return attrs;

)

                    # Format element info
                    attr_str = ", ".join([f'{k}="{v}"' for k, v in attributes.items()])
                    elements_info.append(
                        f"{i+1}. <{tag_name}{attr_str}{text}</{tag_name}>"
                    )

                result = (
                    f"Found {len(elements)} element(s) matching selector '{selector}':\n"
                    + "\n".join(elements_info)
                )

            # Release the browser
            await self._session_manager.release_async_browser(thread_id)

            return result
        except Exception as e:
            return f"Error getting elements: {e!s}"

    def navigate_back(
        self,
        thread_id: str = "default",
    ) -> str:
"""
        Navigate to the previous page (synchronous version).

        Args:
            thread_id (str): Thread ID for the browser session.

        Returns:
            str: Confirmation message.

        """
        try:
            # Get browser and navigate back
            browser = self._session_manager.get_sync_browser(thread_id)
            page = get_current_page(browser)

            # Navigate back
            response = page.go_back()

            # Get the current URL after navigating back
            current_url = page.url if response else "unknown"

            # Release the browser
            self._session_manager.release_sync_browser(thread_id)

            if response:
                return f"Navigated back to {current_url}"
            else:
                return "Could not navigate back (no previous page in history)"
        except Exception as e:
            return f"Error navigating back: {e!s}"

    async def anavigate_back(
        self,
        thread_id: str = "default",
    ) -> str:
"""
        Navigate to the previous page (asynchronous version).

        Args:
            thread_id (str): Thread ID for the browser session.

        Returns:
            str: Confirmation message.

        """
        try:
            # Get browser and navigate back
            browser = await self._session_manager.get_async_browser(thread_id)
            page = await aget_current_page(browser)

            # Navigate back
            response = await page.go_back()

            # Get the current URL after navigating back
            current_url = page.url if response else "unknown"

            # Release the browser
            await self._session_manager.release_async_browser(thread_id)

            if response:
                return f"Navigated back to {current_url}"
            else:
                return "Could not navigate back (no previous page in history)"
        except Exception as e:
            return f"Error navigating back: {e!s}"

    def current_webpage(
        self,
        thread_id: str = "default",
    ) -> str:
"""
        Get information about the current webpage (synchronous version).

        Args:
            thread_id (str): Thread ID for the browser session.

        Returns:
            str: Information about the current webpage.

        """
        try:
            # Get browser and get current webpage info
            browser = self._session_manager.get_sync_browser(thread_id)
            page = get_current_page(browser)

            # Get the current URL
            url = page.url

            # Get the page title
            title = page.title()

            # Get basic page metrics
            metrics = page.evaluate("""
                () => {
                    return {
                        width: document.documentElement.clientWidth,
                        height: document.documentElement.clientHeight,
                        links: document.querySelectorAll('a').length,
                        images: document.querySelectorAll('img').length,
                        forms: document.querySelectorAll('form').length


)

            # Format the result
            result = f"Current webpage information:\n"
            result += f"URL: {url}\n"
            result += f"Title: {title}\n"
            result += f"Viewport size: {metrics['width']}x{metrics['height']}\n"
            result += f"Links: {metrics['links']}\n"
            result += f"Images: {metrics['images']}\n"
            result += f"Forms: {metrics['forms']}"

            # Release the browser
            self._session_manager.release_sync_browser(thread_id)

            return result
        except Exception as e:
            return f"Error getting current webpage information: {e!s}"

    async def acurrent_webpage(
        self,
        thread_id: str = "default",
    ) -> str:
"""
        Get information about the current webpage (asynchronous version).

        Args:
            thread_id (str): Thread ID for the browser session.

        Returns:
            str: Information about the current webpage.

        """
        try:
            # Get browser and get current webpage info
            browser = await self._session_manager.get_async_browser(thread_id)
            page = await aget_current_page(browser)

            # Get the current URL
            url = page.url

            # Get the page title
            title = await page.title()

            # Get basic page metrics
            metrics = await page.evaluate("""
                () => {
                    return {
                        width: document.documentElement.clientWidth,
                        height: document.documentElement.clientHeight,
                        links: document.querySelectorAll('a').length,
                        images: document.querySelectorAll('img').length,
                        forms: document.querySelectorAll('form').length


)

            # Format the result
            result = f"Current webpage information:\n"
            result += f"URL: {url}\n"
            result += f"Title: {title}\n"
            result += f"Viewport size: {metrics['width']}x{metrics['height']}\n"
            result += f"Links: {metrics['links']}\n"
            result += f"Images: {metrics['images']}\n"
            result += f"Forms: {metrics['forms']}"

            # Release the browser
            await self._session_manager.release_async_browser(thread_id)

            return result
        except Exception as e:
            return f"Error getting current webpage information: {e!s}"

    async def cleanup(self, thread_id: Optional[str] = None) -> None:
"""
        Clean up resources

        Args:
            thread_id: Optional thread ID to clean up. If None, cleans up all sessions.

        """
        if thread_id:
            # Clean up a specific thread's session
            if thread_id in self._browser_clients:
                try:
                    self._browser_clients[thread_id].stop()
                    del self._browser_clients[thread_id]
                    logger.info(f"Browser session for thread {thread_id} cleaned up")
                except Exception as e:
                    logger.warning(
                        f"Error stopping browser for thread {thread_id}: {e}"
                    )
        else:
            # Clean up all sessions
            thread_ids = list(self._browser_clients.keys())
            for tid in thread_ids:
                try:
                    self._browser_clients[tid].stop()
                except Exception as e:
                    logger.warning(f"Error stopping browser for thread {tid}: {e}")

            self._browser_clients = {}
            logger.info("All browser sessions cleaned up")

```
  
---|---  
###  navigate_browser [#](https://developers.llamaindex.ai/python/framework-api-reference/tools/aws_bedrock_agentcore/#llama_index.tools.aws_bedrock_agentcore.AgentCoreBrowserToolSpec.navigate_browser "Permanent link")
```
navigate_browser(url: , thread_id:  = 'default') -> 

```

Navigate to a URL (synchronous version).
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`url` |  URL to navigate to. |  _required_  
`thread_id` |  Thread ID for the browser session. |  `'default'`  
Returns:
Name | Type | Description  
---|---|---  
`str` |  Confirmation message.  
Source code in `llama_index/tools/aws_bedrock_agentcore/browser/base.py`
```
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
```
| ```
def navigate_browser(
    self,
    url: str,
    thread_id: str = "default",
) -> str:
"""
    Navigate to a URL (synchronous version).

    Args:
        url (str): URL to navigate to.
        thread_id (str): Thread ID for the browser session.

    Returns:
        str: Confirmation message.

    """
    try:
        # Validate URL scheme
        parsed_url = urlparse(url)
        if parsed_url.scheme not in ("http", "https"):
            return f"URL scheme must be 'http' or 'https', got: {parsed_url.scheme}"

        # Get browser and navigate to URL
        browser = self._session_manager.get_sync_browser(thread_id)
        page = get_current_page(browser)
        response = page.goto(url)
        status = response.status if response else "unknown"

        # Release the browser
        self._session_manager.release_sync_browser(thread_id)

        return f"Navigated to {url} with status code {status}"
    except Exception as e:
        return f"Error navigating to URL: {e!s}"

```
  
---|---  
###  anavigate_browser `async` [#](https://developers.llamaindex.ai/python/framework-api-reference/tools/aws_bedrock_agentcore/#llama_index.tools.aws_bedrock_agentcore.AgentCoreBrowserToolSpec.anavigate_browser "Permanent link")
```
anavigate_browser(url: , thread_id:  = 'default') -> 

```

Navigate to a URL (asynchronous version).
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`url` |  URL to navigate to. |  _required_  
`thread_id` |  Thread ID for the browser session. |  `'default'`  
Returns:
Name | Type | Description  
---|---|---  
`str` |  Confirmation message.  
Source code in `llama_index/tools/aws_bedrock_agentcore/browser/base.py`
```
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
```
| ```
async def anavigate_browser(
    self,
    url: str,
    thread_id: str = "default",
) -> str:
"""
    Navigate to a URL (asynchronous version).

    Args:
        url (str): URL to navigate to.
        thread_id (str): Thread ID for the browser session.

    Returns:
        str: Confirmation message.

    """
    try:
        # Validate URL scheme
        parsed_url = urlparse(url)
        if parsed_url.scheme not in ("http", "https"):
            return f"URL scheme must be 'http' or 'https', got: {parsed_url.scheme}"

        # Get browser and navigate to URL
        browser = await self._session_manager.get_async_browser(thread_id)
        page = await aget_current_page(browser)
        response = await page.goto(url)
        status = response.status if response else "unknown"

        # Release the browser
        await self._session_manager.release_async_browser(thread_id)

        return f"Navigated to {url} with status code {status}"
    except Exception as e:
        return f"Error navigating to URL: {e!s}"

```
  
---|---  
###  click_element [#](https://developers.llamaindex.ai/python/framework-api-reference/tools/aws_bedrock_agentcore/#llama_index.tools.aws_bedrock_agentcore.AgentCoreBrowserToolSpec.click_element "Permanent link")
```
click_element(selector: , thread_id:  = 'default') -> 

```

Click on an element with the given CSS selector (synchronous version).
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`selector` |  CSS selector for the element to click on. |  _required_  
`thread_id` |  Thread ID for the browser session. |  `'default'`  
Returns:
Name | Type | Description  
---|---|---  
`str` |  Confirmation message.  
Source code in `llama_index/tools/aws_bedrock_agentcore/browser/base.py`
```
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
```
| ```
def click_element(
    self,
    selector: str,
    thread_id: str = "default",
) -> str:
"""
    Click on an element with the given CSS selector (synchronous version).

    Args:
        selector (str): CSS selector for the element to click on.
        thread_id (str): Thread ID for the browser session.

    Returns:
        str: Confirmation message.

    """
    try:
        # Get browser and click on element
        browser = self._session_manager.get_sync_browser(thread_id)
        page = get_current_page(browser)

        try:
            page.click(selector, timeout=5000)
            result = f"Clicked on element with selector '{selector}'"
        except Exception as click_error:
            result = f"Unable to click on element with selector '{selector}': {click_error!s}"

        # Release the browser
        self._session_manager.release_sync_browser(thread_id)

        return result
    except Exception as e:
        return f"Error clicking on element: {e!s}"

```
  
---|---  
###  aclick_element `async` [#](https://developers.llamaindex.ai/python/framework-api-reference/tools/aws_bedrock_agentcore/#llama_index.tools.aws_bedrock_agentcore.AgentCoreBrowserToolSpec.aclick_element "Permanent link")
```
aclick_element(selector: , thread_id:  = 'default') -> 

```

Click on an element with the given CSS selector (asynchronous version).
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`selector` |  CSS selector for the element to click on. |  _required_  
`thread_id` |  Thread ID for the browser session. |  `'default'`  
Returns:
Name | Type | Description  
---|---|---  
`str` |  Confirmation message.  
Source code in `llama_index/tools/aws_bedrock_agentcore/browser/base.py`
```
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
```
| ```
async def aclick_element(
    self,
    selector: str,
    thread_id: str = "default",
) -> str:
"""
    Click on an element with the given CSS selector (asynchronous version).

    Args:
        selector (str): CSS selector for the element to click on.
        thread_id (str): Thread ID for the browser session.

    Returns:
        str: Confirmation message.

    """
    try:
        # Get browser and click on element
        browser = await self._session_manager.get_async_browser(thread_id)
        page = await aget_current_page(browser)

        try:
            await page.click(selector, timeout=5000)
            result = f"Clicked on element with selector '{selector}'"
        except Exception as click_error:
            result = f"Unable to click on element with selector '{selector}': {click_error!s}"

        # Release the browser
        await self._session_manager.release_async_browser(thread_id)

        return result
    except Exception as e:
        return f"Error clicking on element: {e!s}"

```
  
---|---  
###  extract_text [#](https://developers.llamaindex.ai/python/framework-api-reference/tools/aws_bedrock_agentcore/#llama_index.tools.aws_bedrock_agentcore.AgentCoreBrowserToolSpec.extract_text "Permanent link")
```
extract_text(selector: Optional[] = None, thread_id:  = 'default') -> 

```

Extract text from the current page (synchronous version).
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`selector` |  `Optional[str]` |  CSS selector for the element to extract text from. If not provided, extracts text from the entire page. |  `None`  
`thread_id` |  Thread ID for the browser session. |  `'default'`  
Returns:
Name | Type | Description  
---|---|---  
`str` |  The extracted text.  
Source code in `llama_index/tools/aws_bedrock_agentcore/browser/base.py`
```
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
```
| ```
def extract_text(
    self,
    selector: Optional[str] = None,
    thread_id: str = "default",
) -> str:
"""
    Extract text from the current page (synchronous version).

    Args:
        selector (Optional[str]): CSS selector for the element to extract text from. If not provided, extracts text from the entire page.
        thread_id (str): Thread ID for the browser session.

    Returns:
        str: The extracted text.

    """
    try:
        # Get browser and extract text
        browser = self._session_manager.get_sync_browser(thread_id)
        page = get_current_page(browser)

        if selector:
            try:
                element = page.query_selector(selector)
                if element:
                    text = element.text_content()
                    result = text if text else "Element found but contains no text"
                else:
                    result = f"No element found with selector '{selector}'"
            except Exception as selector_error:
                result = f"Error extracting text from selector '{selector}': {selector_error!s}"
        else:
            # Extract text from the entire page
            result = page.content()

        # Release the browser
        self._session_manager.release_sync_browser(thread_id)

        return result
    except Exception as e:
        return f"Error extracting text: {e!s}"

```
  
---|---  
###  aextract_text `async` [#](https://developers.llamaindex.ai/python/framework-api-reference/tools/aws_bedrock_agentcore/#llama_index.tools.aws_bedrock_agentcore.AgentCoreBrowserToolSpec.aextract_text "Permanent link")
```
aextract_text(selector: Optional[] = None, thread_id:  = 'default') -> 

```

Extract text from the current page (asynchronous version).
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`selector` |  `Optional[str]` |  CSS selector for the element to extract text from. If not provided, extracts text from the entire page. |  `None`  
`thread_id` |  Thread ID for the browser session. |  `'default'`  
Returns:
Name | Type | Description  
---|---|---  
`str` |  The extracted text.  
Source code in `llama_index/tools/aws_bedrock_agentcore/browser/base.py`
```
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
```
| ```
async def aextract_text(
    self,
    selector: Optional[str] = None,
    thread_id: str = "default",
) -> str:
"""
    Extract text from the current page (asynchronous version).

    Args:
        selector (Optional[str]): CSS selector for the element to extract text from. If not provided, extracts text from the entire page.
        thread_id (str): Thread ID for the browser session.

    Returns:
        str: The extracted text.

    """
    try:
        # Get browser and extract text
        browser = await self._session_manager.get_async_browser(thread_id)
        page = await aget_current_page(browser)

        if selector:
            try:
                element = await page.query_selector(selector)
                if element:
                    text = await element.text_content()
                    result = text if text else "Element found but contains no text"
                else:
                    result = f"No element found with selector '{selector}'"
            except Exception as selector_error:
                result = f"Error extracting text from selector '{selector}': {selector_error!s}"
        else:
            # Extract text from the entire page
            result = await page.content()

        # Release the browser
        await self._session_manager.release_async_browser(thread_id)

        return result
    except Exception as e:
        return f"Error extracting text: {e!s}"

```
  
---|---  
###  extract_hyperlinks [#](https://developers.llamaindex.ai/python/framework-api-reference/tools/aws_bedrock_agentcore/#llama_index.tools.aws_bedrock_agentcore.AgentCoreBrowserToolSpec.extract_hyperlinks "Permanent link")
```
extract_hyperlinks(thread_id:  = 'default') -> 

```

Extract hyperlinks from the current page (synchronous version).
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`thread_id` |  Thread ID for the browser session. |  `'default'`  
Returns:
Name | Type | Description  
---|---|---  
`str` |  The extracted hyperlinks.  
Source code in `llama_index/tools/aws_bedrock_agentcore/browser/base.py`
```
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
```
| ```
def extract_hyperlinks(
    self,
    thread_id: str = "default",
) -> str:
"""
    Extract hyperlinks from the current page (synchronous version).

    Args:
        thread_id (str): Thread ID for the browser session.

    Returns:
        str: The extracted hyperlinks.

    """
    try:
        # Get browser and extract hyperlinks
        browser = self._session_manager.get_sync_browser(thread_id)
        page = get_current_page(browser)

        # Extract all hyperlinks from the page
        links = page.eval_on_selector_all(
            "a[href]",
"""
            (elements) => {
                return elements.map(el => {
                    return {
                        text: el.innerText || el.textContent,
                        href: el.href



        """,
        )

        # Format the links
        formatted_links = []
        for i, link in enumerate(links):
            formatted_links.append(
                f"{i+1}. {link.get('text','No text')}: {link.get('href','No href')}"
            )

        result = (
            "\n".join(formatted_links)
            if formatted_links
            else "No hyperlinks found on the page"
        )

        # Release the browser
        self._session_manager.release_sync_browser(thread_id)

        return result
    except Exception as e:
        return f"Error extracting hyperlinks: {e!s}"

```
  
---|---  
###  aextract_hyperlinks `async` [#](https://developers.llamaindex.ai/python/framework-api-reference/tools/aws_bedrock_agentcore/#llama_index.tools.aws_bedrock_agentcore.AgentCoreBrowserToolSpec.aextract_hyperlinks "Permanent link")
```
aextract_hyperlinks(thread_id:  = 'default') -> 

```

Extract hyperlinks from the current page (asynchronous version).
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`thread_id` |  Thread ID for the browser session. |  `'default'`  
Returns:
Name | Type | Description  
---|---|---  
`str` |  The extracted hyperlinks.  
Source code in `llama_index/tools/aws_bedrock_agentcore/browser/base.py`
```
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
```
| ```
async def aextract_hyperlinks(
    self,
    thread_id: str = "default",
) -> str:
"""
    Extract hyperlinks from the current page (asynchronous version).

    Args:
        thread_id (str): Thread ID for the browser session.

    Returns:
        str: The extracted hyperlinks.

    """
    try:
        # Get browser and extract hyperlinks
        browser = await self._session_manager.get_async_browser(thread_id)
        page = await aget_current_page(browser)

        # Extract all hyperlinks from the page
        links = await page.eval_on_selector_all(
            "a[href]",
"""
            (elements) => {
                return elements.map(el => {
                    return {
                        text: el.innerText || el.textContent,
                        href: el.href



        """,
        )

        # Format the links
        formatted_links = []
        for i, link in enumerate(links):
            formatted_links.append(
                f"{i+1}. {link.get('text','No text')}: {link.get('href','No href')}"
            )

        result = (
            "\n".join(formatted_links)
            if formatted_links
            else "No hyperlinks found on the page"
        )

        # Release the browser
        await self._session_manager.release_async_browser(thread_id)

        return result
    except Exception as e:
        return f"Error extracting hyperlinks: {e!s}"

```
  
---|---  
###  get_elements [#](https://developers.llamaindex.ai/python/framework-api-reference/tools/aws_bedrock_agentcore/#llama_index.tools.aws_bedrock_agentcore.AgentCoreBrowserToolSpec.get_elements "Permanent link")
```
get_elements(selector: , thread_id:  = 'default') -> 

```

Get elements matching a CSS selector (synchronous version).
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`selector` |  CSS selector for the elements to get. |  _required_  
`thread_id` |  Thread ID for the browser session. |  `'default'`  
Returns:
Name | Type | Description  
---|---|---  
`str` |  Information about the matching elements.  
Source code in `llama_index/tools/aws_bedrock_agentcore/browser/base.py`
```
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
```
| ```
def get_elements(
    self,
    selector: str,
    thread_id: str = "default",
) -> str:
"""
    Get elements matching a CSS selector (synchronous version).

    Args:
        selector (str): CSS selector for the elements to get.
        thread_id (str): Thread ID for the browser session.

    Returns:
        str: Information about the matching elements.

    """
    try:
        # Get browser and find elements
        browser = self._session_manager.get_sync_browser(thread_id)
        page = get_current_page(browser)

        # Find elements matching the selector
        elements = page.query_selector_all(selector)

        if not elements:
            result = f"No elements found matching selector '{selector}'"
        else:
            # Extract information about the elements
            elements_info = []
            for i, element in enumerate(elements):
                tag_name = element.evaluate("el => el.tagName.toLowerCase()")
                text = element.text_content() or ""
                attributes = element.evaluate("""
                    (el) => {
                        const attrs = {};
                        for (const attr of el.attributes) {
                            attrs[attr.name] = attr.value;

                        return attrs;

)

                # Format element info
                attr_str = ", ".join([f'{k}="{v}"' for k, v in attributes.items()])
                elements_info.append(
                    f"{i+1}. <{tag_name}{attr_str}{text}</{tag_name}>"
                )

            result = (
                f"Found {len(elements)} element(s) matching selector '{selector}':\n"
                + "\n".join(elements_info)
            )

        # Release the browser
        self._session_manager.release_sync_browser(thread_id)

        return result
    except Exception as e:
        return f"Error getting elements: {e!s}"

```
  
---|---  
###  aget_elements `async` [#](https://developers.llamaindex.ai/python/framework-api-reference/tools/aws_bedrock_agentcore/#llama_index.tools.aws_bedrock_agentcore.AgentCoreBrowserToolSpec.aget_elements "Permanent link")
```
aget_elements(selector: , thread_id:  = 'default') -> 

```

Get elements matching a CSS selector (asynchronous version).
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`selector` |  CSS selector for the elements to get. |  _required_  
`thread_id` |  Thread ID for the browser session. |  `'default'`  
Returns:
Name | Type | Description  
---|---|---  
`str` |  Information about the matching elements.  
Source code in `llama_index/tools/aws_bedrock_agentcore/browser/base.py`
```
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
```
| ```
async def aget_elements(
    self,
    selector: str,
    thread_id: str = "default",
) -> str:
"""
    Get elements matching a CSS selector (asynchronous version).

    Args:
        selector (str): CSS selector for the elements to get.
        thread_id (str): Thread ID for the browser session.

    Returns:
        str: Information about the matching elements.

    """
    try:
        # Get browser and find elements
        browser = await self._session_manager.get_async_browser(thread_id)
        page = await aget_current_page(browser)

        # Find elements matching the selector
        elements = await page.query_selector_all(selector)

        if not elements:
            result = f"No elements found matching selector '{selector}'"
        else:
            # Extract information about the elements
            elements_info = []
            for i, element in enumerate(elements):
                tag_name = await element.evaluate("el => el.tagName.toLowerCase()")
                text = await element.text_content() or ""
                attributes = await element.evaluate("""
                    (el) => {
                        const attrs = {};
                        for (const attr of el.attributes) {
                            attrs[attr.name] = attr.value;

                        return attrs;

)

                # Format element info
                attr_str = ", ".join([f'{k}="{v}"' for k, v in attributes.items()])
                elements_info.append(
                    f"{i+1}. <{tag_name}{attr_str}{text}</{tag_name}>"
                )

            result = (
                f"Found {len(elements)} element(s) matching selector '{selector}':\n"
                + "\n".join(elements_info)
            )

        # Release the browser
        await self._session_manager.release_async_browser(thread_id)

        return result
    except Exception as e:
        return f"Error getting elements: {e!s}"

```
  
---|---  
###  navigate_back [#](https://developers.llamaindex.ai/python/framework-api-reference/tools/aws_bedrock_agentcore/#llama_index.tools.aws_bedrock_agentcore.AgentCoreBrowserToolSpec.navigate_back "Permanent link")
```
navigate_back(thread_id:  = 'default') -> 

```

Navigate to the previous page (synchronous version).
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`thread_id` |  Thread ID for the browser session. |  `'default'`  
Returns:
Name | Type | Description  
---|---|---  
`str` |  Confirmation message.  
Source code in `llama_index/tools/aws_bedrock_agentcore/browser/base.py`
```
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
```
| ```
def navigate_back(
    self,
    thread_id: str = "default",
) -> str:
"""
    Navigate to the previous page (synchronous version).

    Args:
        thread_id (str): Thread ID for the browser session.

    Returns:
        str: Confirmation message.

    """
    try:
        # Get browser and navigate back
        browser = self._session_manager.get_sync_browser(thread_id)
        page = get_current_page(browser)

        # Navigate back
        response = page.go_back()

        # Get the current URL after navigating back
        current_url = page.url if response else "unknown"

        # Release the browser
        self._session_manager.release_sync_browser(thread_id)

        if response:
            return f"Navigated back to {current_url}"
        else:
            return "Could not navigate back (no previous page in history)"
    except Exception as e:
        return f"Error navigating back: {e!s}"

```
  
---|---  
###  anavigate_back `async` [#](https://developers.llamaindex.ai/python/framework-api-reference/tools/aws_bedrock_agentcore/#llama_index.tools.aws_bedrock_agentcore.AgentCoreBrowserToolSpec.anavigate_back "Permanent link")
```
anavigate_back(thread_id:  = 'default') -> 

```

Navigate to the previous page (asynchronous version).
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`thread_id` |  Thread ID for the browser session. |  `'default'`  
Returns:
Name | Type | Description  
---|---|---  
`str` |  Confirmation message.  
Source code in `llama_index/tools/aws_bedrock_agentcore/browser/base.py`
```
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
```
| ```
async def anavigate_back(
    self,
    thread_id: str = "default",
) -> str:
"""
    Navigate to the previous page (asynchronous version).

    Args:
        thread_id (str): Thread ID for the browser session.

    Returns:
        str: Confirmation message.

    """
    try:
        # Get browser and navigate back
        browser = await self._session_manager.get_async_browser(thread_id)
        page = await aget_current_page(browser)

        # Navigate back
        response = await page.go_back()

        # Get the current URL after navigating back
        current_url = page.url if response else "unknown"

        # Release the browser
        await self._session_manager.release_async_browser(thread_id)

        if response:
            return f"Navigated back to {current_url}"
        else:
            return "Could not navigate back (no previous page in history)"
    except Exception as e:
        return f"Error navigating back: {e!s}"

```
  
---|---  
###  current_webpage [#](https://developers.llamaindex.ai/python/framework-api-reference/tools/aws_bedrock_agentcore/#llama_index.tools.aws_bedrock_agentcore.AgentCoreBrowserToolSpec.current_webpage "Permanent link")
```
current_webpage(thread_id:  = 'default') -> 

```

Get information about the current webpage (synchronous version).
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`thread_id` |  Thread ID for the browser session. |  `'default'`  
Returns:
Name | Type | Description  
---|---|---  
`str` |  Information about the current webpage.  
Source code in `llama_index/tools/aws_bedrock_agentcore/browser/base.py`
```
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
```
| ```
def current_webpage(
    self,
    thread_id: str = "default",
) -> str:
"""
    Get information about the current webpage (synchronous version).

    Args:
        thread_id (str): Thread ID for the browser session.

    Returns:
        str: Information about the current webpage.

    """
    try:
        # Get browser and get current webpage info
        browser = self._session_manager.get_sync_browser(thread_id)
        page = get_current_page(browser)

        # Get the current URL
        url = page.url

        # Get the page title
        title = page.title()

        # Get basic page metrics
        metrics = page.evaluate("""
            () => {
                return {
                    width: document.documentElement.clientWidth,
                    height: document.documentElement.clientHeight,
                    links: document.querySelectorAll('a').length,
                    images: document.querySelectorAll('img').length,
                    forms: document.querySelectorAll('form').length


        """)

        # Format the result
        result = f"Current webpage information:\n"
        result += f"URL: {url}\n"
        result += f"Title: {title}\n"
        result += f"Viewport size: {metrics['width']}x{metrics['height']}\n"
        result += f"Links: {metrics['links']}\n"
        result += f"Images: {metrics['images']}\n"
        result += f"Forms: {metrics['forms']}"

        # Release the browser
        self._session_manager.release_sync_browser(thread_id)

        return result
    except Exception as e:
        return f"Error getting current webpage information: {e!s}"

```
  
---|---  
###  acurrent_webpage `async` [#](https://developers.llamaindex.ai/python/framework-api-reference/tools/aws_bedrock_agentcore/#llama_index.tools.aws_bedrock_agentcore.AgentCoreBrowserToolSpec.acurrent_webpage "Permanent link")
```
acurrent_webpage(thread_id:  = 'default') -> 

```

Get information about the current webpage (asynchronous version).
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`thread_id` |  Thread ID for the browser session. |  `'default'`  
Returns:
Name | Type | Description  
---|---|---  
`str` |  Information about the current webpage.  
Source code in `llama_index/tools/aws_bedrock_agentcore/browser/base.py`
```
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
```
| ```
async def acurrent_webpage(
    self,
    thread_id: str = "default",
) -> str:
"""
    Get information about the current webpage (asynchronous version).

    Args:
        thread_id (str): Thread ID for the browser session.

    Returns:
        str: Information about the current webpage.

    """
    try:
        # Get browser and get current webpage info
        browser = await self._session_manager.get_async_browser(thread_id)
        page = await aget_current_page(browser)

        # Get the current URL
        url = page.url

        # Get the page title
        title = await page.title()

        # Get basic page metrics
        metrics = await page.evaluate("""
            () => {
                return {
                    width: document.documentElement.clientWidth,
                    height: document.documentElement.clientHeight,
                    links: document.querySelectorAll('a').length,
                    images: document.querySelectorAll('img').length,
                    forms: document.querySelectorAll('form').length


        """)

        # Format the result
        result = f"Current webpage information:\n"
        result += f"URL: {url}\n"
        result += f"Title: {title}\n"
        result += f"Viewport size: {metrics['width']}x{metrics['height']}\n"
        result += f"Links: {metrics['links']}\n"
        result += f"Images: {metrics['images']}\n"
        result += f"Forms: {metrics['forms']}"

        # Release the browser
        await self._session_manager.release_async_browser(thread_id)

        return result
    except Exception as e:
        return f"Error getting current webpage information: {e!s}"

```
  
---|---  
###  cleanup `async` [#](https://developers.llamaindex.ai/python/framework-api-reference/tools/aws_bedrock_agentcore/#llama_index.tools.aws_bedrock_agentcore.AgentCoreBrowserToolSpec.cleanup "Permanent link")
```
cleanup(thread_id: Optional[] = None) -> None

```

Clean up resources
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`thread_id` |  `Optional[str]` |  Optional thread ID to clean up. If None, cleans up all sessions. |  `None`  
Source code in `llama_index/tools/aws_bedrock_agentcore/browser/base.py`
```
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
```
| ```
async def cleanup(self, thread_id: Optional[str] = None) -> None:
"""
    Clean up resources

    Args:
        thread_id: Optional thread ID to clean up. If None, cleans up all sessions.

    """
    if thread_id:
        # Clean up a specific thread's session
        if thread_id in self._browser_clients:
            try:
                self._browser_clients[thread_id].stop()
                del self._browser_clients[thread_id]
                logger.info(f"Browser session for thread {thread_id} cleaned up")
            except Exception as e:
                logger.warning(
                    f"Error stopping browser for thread {thread_id}: {e}"
                )
    else:
        # Clean up all sessions
        thread_ids = list(self._browser_clients.keys())
        for tid in thread_ids:
            try:
                self._browser_clients[tid].stop()
            except Exception as e:
                logger.warning(f"Error stopping browser for thread {tid}: {e}")

        self._browser_clients = {}
        logger.info("All browser sessions cleaned up")

```
  
---|---  
##  AgentCoreCodeInterpreterToolSpec [#](https://developers.llamaindex.ai/python/framework-api-reference/tools/aws_bedrock_agentcore/#llama_index.tools.aws_bedrock_agentcore.AgentCoreCodeInterpreterToolSpec "Permanent link")
Bases: 
AWS Bedrock AgentCore Code Interpreter Tool Spec.
This toolkit provides a set of tools for working with a remote code interpreter environment:
  * execute_code - Run code in various languages (primarily Python)
  * execute_command - Run shell commands
  * read_files - Read content of files in the environment
  * list_files - List files in directories
  * delete_files - Remove files from the environment
  * write_files - Create or update files
  * start_command - Start long-running commands asynchronously
  * get_task - Check status of async tasks
  * stop_task - Stop running tasks


The toolkit lazily initializes the code interpreter session on first use. It supports multiple threads by maintaining separate code interpreter sessions for each thread ID.
Source code in `llama_index/tools/aws_bedrock_agentcore/code_interpreter/base.py`
```
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
```
| ```
class AgentCoreCodeInterpreterToolSpec(BaseToolSpec):
"""
    AWS Bedrock AgentCore Code Interpreter Tool Spec.

    This toolkit provides a set of tools for working with a remote code interpreter environment:

    * execute_code - Run code in various languages (primarily Python)
    * execute_command - Run shell commands
    * read_files - Read content of files in the environment
    * list_files - List files in directories
    * delete_files - Remove files from the environment
    * write_files - Create or update files
    * start_command - Start long-running commands asynchronously
    * get_task - Check status of async tasks
    * stop_task - Stop running tasks

    The toolkit lazily initializes the code interpreter session on first use.
    It supports multiple threads by maintaining separate code interpreter sessions for each thread ID.
    """

    spec_functions = [
        ("execute_code", "aexecute_code"),
        ("execute_command", "aexecute_command"),
        ("read_files", "aread_files"),
        ("list_files", "alist_files"),
        ("delete_files", "adelete_files"),
        ("write_files", "awrite_files"),
        ("start_command", "astart_command"),
        ("get_task", "aget_task"),
        ("stop_task", "astop_task"),
    ]

    def __init__(self, region: Optional[str] = None) -> None:
"""
        Initialize the AWS Bedrock AgentCore Code Interpreter Tool Spec.

        Args:
            region (Optional[str]): AWS region to use for Bedrock AgentCore services.
                If not provided, will try to get it from environment variables.

        """
        self.region = region if region is not None else get_aws_region()
        self._code_interpreters: Dict[str, CodeInterpreter] = {}

    def _get_or_create_interpreter(self, thread_id: str = "default") -> CodeInterpreter:
"""
        Get or create a code interpreter for the specified thread.

        Args:
            thread_id: Thread ID for the code interpreter session

        Returns:
            CodeInterpreter instance

        """
        if thread_id in self._code_interpreters:
            return self._code_interpreters[thread_id]

        # Create a new code interpreter for this thread
        code_interpreter = CodeInterpreter(region=self.region)
        code_interpreter.start()
        logger.info(
            f"Started code interpreter with session_id:{code_interpreter.session_id} for thread:{thread_id}"
        )

        # Store the interpreter
        self._code_interpreters[thread_id] = code_interpreter
        return code_interpreter

    def execute_code(
        self,
        code: str,
        language: str = "python",
        clear_context: bool = False,
        thread_id: str = "default",
    ) -> str:
"""
        Execute code in the code interpreter sandbox (synchronous version).

        Args:
            code (str): The code to execute.
            language (str): The programming language of the code. Default is "python".
            clear_context (bool): Whether to clear execution context. Default is False.
            thread_id (str): Thread ID for the code interpreter session. Default is "default".

        Returns:
            str: The result of the code execution.

        """
        try:
            # Get or create code interpreter
            code_interpreter = self._get_or_create_interpreter(thread_id=thread_id)

            # Execute code
            response = code_interpreter.invoke(
                method="executeCode",
                params={
                    "code": code,
                    "language": language,
                    "clearContext": clear_context,
                },
            )

            return extract_output_from_stream(response)
        except Exception as e:
            return f"Error executing code: {e!s}"

    async def aexecute_code(
        self,
        code: str,
        language: str = "python",
        clear_context: bool = False,
        thread_id: str = "default",
    ) -> str:
"""
        Execute code in the code interpreter sandbox (asynchronous version).

        Args:
            code (str): The code to execute.
            language (str): The programming language of the code. Default is "python".
            clear_context (bool): Whether to clear execution context. Default is False.
            thread_id (str): Thread ID for the code interpreter session. Default is "default".

        Returns:
            str: The result of the code execution.

        """
        # Use the synchronous version as the underlying API is thread-safe
        return self.execute_code(
            code=code,
            language=language,
            clear_context=clear_context,
            thread_id=thread_id,
        )

    def execute_command(
        self,
        command: str,
        thread_id: str = "default",
    ) -> str:
"""
        Execute a shell command in the code interpreter sandbox (synchronous version).

        Args:
            command (str): The command to execute.
            thread_id (str): Thread ID for the code interpreter session. Default is "default".

        Returns:
            str: The result of the command execution.

        """
        try:
            # Get or create code interpreter
            code_interpreter = self._get_or_create_interpreter(thread_id=thread_id)

            # Execute command
            response = code_interpreter.invoke(
                method="executeCommand", params={"command": command}
            )

            return extract_output_from_stream(response)
        except Exception as e:
            return f"Error executing command: {e!s}"

    async def aexecute_command(
        self,
        command: str,
        thread_id: str = "default",
    ) -> str:
"""
        Execute a shell command in the code interpreter sandbox (asynchronous version).

        Args:
            command (str): The command to execute.
            thread_id (str): Thread ID for the code interpreter session. Default is "default".

        Returns:
            str: The result of the command execution.

        """
        # Use the synchronous version as the underlying API is thread-safe
        return self.execute_command(command=command, thread_id=thread_id)

    def read_files(
        self,
        paths: List[str],
        thread_id: str = "default",
    ) -> str:
"""
        Read content of files in the environment (synchronous version).

        Args:
            paths (List[str]): List of file paths to read.
            thread_id (str): Thread ID for the code interpreter session. Default is "default".

        Returns:
            str: The content of the files.

        """
        try:
            # Get or create code interpreter
            code_interpreter = self._get_or_create_interpreter(thread_id=thread_id)

            # Read files
            response = code_interpreter.invoke(
                method="readFiles", params={"paths": paths}
            )

            return extract_output_from_stream(response)
        except Exception as e:
            return f"Error reading files: {e!s}"

    async def aread_files(
        self,
        paths: List[str],
        thread_id: str = "default",
    ) -> str:
"""
        Read content of files in the environment (asynchronous version).

        Args:
            paths (List[str]): List of file paths to read.
            thread_id (str): Thread ID for the code interpreter session. Default is "default".

        Returns:
            str: The content of the files.

        """
        # Use the synchronous version as the underlying API is thread-safe
        return self.read_files(paths=paths, thread_id=thread_id)

    def list_files(
        self,
        directory_path: str = "",
        thread_id: str = "default",
    ) -> str:
"""
        List files in directories in the environment (synchronous version).

        Args:
            directory_path (str): Path to the directory to list. Default is current directory.
            thread_id (str): Thread ID for the code interpreter session. Default is "default".

        Returns:
            str: The list of files.

        """
        try:
            # Get or create code interpreter
            code_interpreter = self._get_or_create_interpreter(thread_id=thread_id)

            # List files
            response = code_interpreter.invoke(
                method="listFiles", params={"directoryPath": directory_path}
            )

            return extract_output_from_stream(response)
        except Exception as e:
            return f"Error listing files: {e!s}"

    async def alist_files(
        self,
        directory_path: str = "",
        thread_id: str = "default",
    ) -> str:
"""
        List files in directories in the environment (asynchronous version).

        Args:
            directory_path (str): Path to the directory to list. Default is current directory.
            thread_id (str): Thread ID for the code interpreter session. Default is "default".

        Returns:
            str: The list of files.

        """
        # Use the synchronous version as the underlying API is thread-safe
        return self.list_files(directory_path=directory_path, thread_id=thread_id)

    def delete_files(
        self,
        paths: List[str],
        thread_id: str = "default",
    ) -> str:
"""
        Remove files from the environment (synchronous version).

        Args:
            paths (List[str]): List of file paths to delete.
            thread_id (str): Thread ID for the code interpreter session. Default is "default".

        Returns:
            str: The result of the delete operation.

        """
        try:
            # Get or create code interpreter
            code_interpreter = self._get_or_create_interpreter(thread_id=thread_id)

            # Remove files
            response = code_interpreter.invoke(
                method="removeFiles", params={"paths": paths}
            )

            return extract_output_from_stream(response)
        except Exception as e:
            return f"Error deleting files: {e!s}"

    async def adelete_files(
        self,
        paths: List[str],
        thread_id: str = "default",
    ) -> str:
"""
        Remove files from the environment (asynchronous version).

        Args:
            paths (List[str]): List of file paths to delete.
            thread_id (str): Thread ID for the code interpreter session. Default is "default".

        Returns:
            str: The result of the delete operation.

        """
        # Use the synchronous version as the underlying API is thread-safe
        return self.delete_files(paths=paths, thread_id=thread_id)

    def write_files(
        self,
        files: List[Dict[str, str]],
        thread_id: str = "default",
    ) -> str:
"""
        Create or update files in the environment (synchronous version).

        Args:
            files (List[Dict[str, str]]): List of dictionaries with path and text fields.
            thread_id (str): Thread ID for the code interpreter session. Default is "default".

        Returns:
            str: The result of the write operation.

        """
        try:
            # Get or create code interpreter
            code_interpreter = self._get_or_create_interpreter(thread_id=thread_id)

            # Write files
            response = code_interpreter.invoke(
                method="writeFiles", params={"content": files}
            )

            return extract_output_from_stream(response)
        except Exception as e:
            return f"Error writing files: {e!s}"

    async def awrite_files(
        self,
        files: List[Dict[str, str]],
        thread_id: str = "default",
    ) -> str:
"""
        Create or update files in the environment (asynchronous version).

        Args:
            files (List[Dict[str, str]]): List of dictionaries with path and text fields.
            thread_id (str): Thread ID for the code interpreter session. Default is "default".

        Returns:
            str: The result of the write operation.

        """
        # Use the synchronous version as the underlying API is thread-safe
        return self.write_files(files=files, thread_id=thread_id)

    def start_command(
        self,
        command: str,
        thread_id: str = "default",
    ) -> str:
"""
        Start a long-running command asynchronously (synchronous version).

        Args:
            command (str): The command to execute asynchronously.
            thread_id (str): Thread ID for the code interpreter session. Default is "default".

        Returns:
            str: The task ID and status.

        """
        try:
            # Get or create code interpreter
            code_interpreter = self._get_or_create_interpreter(thread_id=thread_id)

            # Start command execution
            response = code_interpreter.invoke(
                method="startCommandExecution", params={"command": command}
            )

            return extract_output_from_stream(response)
        except Exception as e:
            return f"Error starting command: {e!s}"

    async def astart_command(
        self,
        command: str,
        thread_id: str = "default",
    ) -> str:
"""
        Start a long-running command asynchronously (asynchronous version).

        Args:
            command (str): The command to execute asynchronously.
            thread_id (str): Thread ID for the code interpreter session. Default is "default".

        Returns:
            str: The task ID and status.

        """
        # Use the synchronous version as the underlying API is thread-safe
        return self.start_command(command=command, thread_id=thread_id)

    def get_task(
        self,
        task_id: str,
        thread_id: str = "default",
    ) -> str:
"""
        Check status of an async task (synchronous version).

        Args:
            task_id (str): The ID of the task to check.
            thread_id (str): Thread ID for the code interpreter session. Default is "default".

        Returns:
            str: The task status.

        """
        try:
            # Get or create code interpreter
            code_interpreter = self._get_or_create_interpreter(thread_id=thread_id)

            # Get task status
            response = code_interpreter.invoke(
                method="getTask", params={"taskId": task_id}
            )

            return extract_output_from_stream(response)
        except Exception as e:
            return f"Error getting task status: {e!s}"

    async def aget_task(
        self,
        task_id: str,
        thread_id: str = "default",
    ) -> str:
"""
        Check status of an async task (asynchronous version).

        Args:
            task_id (str): The ID of the task to check.
            thread_id (str): Thread ID for the code interpreter session. Default is "default".

        Returns:
            str: The task status.

        """
        # Use the synchronous version as the underlying API is thread-safe
        return self.get_task(task_id=task_id, thread_id=thread_id)

    def stop_task(
        self,
        task_id: str,
        thread_id: str = "default",
    ) -> str:
"""
        Stop a running task (synchronous version).

        Args:
            task_id (str): The ID of the task to stop.
            thread_id (str): Thread ID for the code interpreter session. Default is "default".

        Returns:
            str: The result of the stop operation.

        """
        try:
            # Get or create code interpreter
            code_interpreter = self._get_or_create_interpreter(thread_id=thread_id)

            # Stop task
            response = code_interpreter.invoke(
                method="stopTask", params={"taskId": task_id}
            )

            return extract_output_from_stream(response)
        except Exception as e:
            return f"Error stopping task: {e!s}"

    async def astop_task(
        self,
        task_id: str,
        thread_id: str = "default",
    ) -> str:
"""
        Stop a running task (asynchronous version).

        Args:
            task_id (str): The ID of the task to stop.
            thread_id (str): Thread ID for the code interpreter session. Default is "default".

        Returns:
            str: The result of the stop operation.

        """
        # Use the synchronous version as the underlying API is thread-safe
        return self.stop_task(task_id=task_id, thread_id=thread_id)

    async def cleanup(self, thread_id: Optional[str] = None) -> None:
"""
        Clean up resources

        Args:
            thread_id: Optional thread ID to clean up. If None, cleans up all sessions.

        """
        if thread_id:
            # Clean up a specific thread's session
            if thread_id in self._code_interpreters:
                try:
                    self._code_interpreters[thread_id].stop()
                    del self._code_interpreters[thread_id]
                    logger.info(
                        f"Code interpreter session for thread {thread_id} cleaned up"
                    )
                except Exception as e:
                    logger.warning(
                        f"Error stopping code interpreter for thread {thread_id}: {e}"
                    )
        else:
            # Clean up all sessions
            thread_ids = list(self._code_interpreters.keys())
            for tid in thread_ids:
                try:
                    self._code_interpreters[tid].stop()
                except Exception as e:
                    logger.warning(
                        f"Error stopping code interpreter for thread {tid}: {e}"
                    )

            self._code_interpreters = {}
            logger.info("All code interpreter sessions cleaned up")

```
  
---|---  
###  execute_code [#](https://developers.llamaindex.ai/python/framework-api-reference/tools/aws_bedrock_agentcore/#llama_index.tools.aws_bedrock_agentcore.AgentCoreCodeInterpreterToolSpec.execute_code "Permanent link")
```
execute_code(code: , language:  = 'python', clear_context:  = False, thread_id:  = 'default') -> 

```

Execute code in the code interpreter sandbox (synchronous version).
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`code` |  The code to execute. |  _required_  
`language` |  The programming language of the code. Default is "python". |  `'python'`  
`clear_context` |  `bool` |  Whether to clear execution context. Default is False. |  `False`  
`thread_id` |  Thread ID for the code interpreter session. Default is "default". |  `'default'`  
Returns:
Name | Type | Description  
---|---|---  
`str` |  The result of the code execution.  
Source code in `llama_index/tools/aws_bedrock_agentcore/code_interpreter/base.py`
```
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
```
| ```
def execute_code(
    self,
    code: str,
    language: str = "python",
    clear_context: bool = False,
    thread_id: str = "default",
) -> str:
"""
    Execute code in the code interpreter sandbox (synchronous version).

    Args:
        code (str): The code to execute.
        language (str): The programming language of the code. Default is "python".
        clear_context (bool): Whether to clear execution context. Default is False.
        thread_id (str): Thread ID for the code interpreter session. Default is "default".

    Returns:
        str: The result of the code execution.

    """
    try:
        # Get or create code interpreter
        code_interpreter = self._get_or_create_interpreter(thread_id=thread_id)

        # Execute code
        response = code_interpreter.invoke(
            method="executeCode",
            params={
                "code": code,
                "language": language,
                "clearContext": clear_context,
            },
        )

        return extract_output_from_stream(response)
    except Exception as e:
        return f"Error executing code: {e!s}"

```
  
---|---  
###  aexecute_code `async` [#](https://developers.llamaindex.ai/python/framework-api-reference/tools/aws_bedrock_agentcore/#llama_index.tools.aws_bedrock_agentcore.AgentCoreCodeInterpreterToolSpec.aexecute_code "Permanent link")
```
aexecute_code(code: , language:  = 'python', clear_context:  = False, thread_id:  = 'default') -> 

```

Execute code in the code interpreter sandbox (asynchronous version).
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`code` |  The code to execute. |  _required_  
`language` |  The programming language of the code. Default is "python". |  `'python'`  
`clear_context` |  `bool` |  Whether to clear execution context. Default is False. |  `False`  
`thread_id` |  Thread ID for the code interpreter session. Default is "default". |  `'default'`  
Returns:
Name | Type | Description  
---|---|---  
`str` |  The result of the code execution.  
Source code in `llama_index/tools/aws_bedrock_agentcore/code_interpreter/base.py`
```
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
```
| ```
async def aexecute_code(
    self,
    code: str,
    language: str = "python",
    clear_context: bool = False,
    thread_id: str = "default",
) -> str:
"""
    Execute code in the code interpreter sandbox (asynchronous version).

    Args:
        code (str): The code to execute.
        language (str): The programming language of the code. Default is "python".
        clear_context (bool): Whether to clear execution context. Default is False.
        thread_id (str): Thread ID for the code interpreter session. Default is "default".

    Returns:
        str: The result of the code execution.

    """
    # Use the synchronous version as the underlying API is thread-safe
    return self.execute_code(
        code=code,
        language=language,
        clear_context=clear_context,
        thread_id=thread_id,
    )

```
  
---|---  
###  execute_command [#](https://developers.llamaindex.ai/python/framework-api-reference/tools/aws_bedrock_agentcore/#llama_index.tools.aws_bedrock_agentcore.AgentCoreCodeInterpreterToolSpec.execute_command "Permanent link")
```
execute_command(command: , thread_id:  = 'default') -> 

```

Execute a shell command in the code interpreter sandbox (synchronous version).
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`command` |  The command to execute. |  _required_  
`thread_id` |  Thread ID for the code interpreter session. Default is "default". |  `'default'`  
Returns:
Name | Type | Description  
---|---|---  
`str` |  The result of the command execution.  
Source code in `llama_index/tools/aws_bedrock_agentcore/code_interpreter/base.py`
```
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
```
| ```
def execute_command(
    self,
    command: str,
    thread_id: str = "default",
) -> str:
"""
    Execute a shell command in the code interpreter sandbox (synchronous version).

    Args:
        command (str): The command to execute.
        thread_id (str): Thread ID for the code interpreter session. Default is "default".

    Returns:
        str: The result of the command execution.

    """
    try:
        # Get or create code interpreter
        code_interpreter = self._get_or_create_interpreter(thread_id=thread_id)

        # Execute command
        response = code_interpreter.invoke(
            method="executeCommand", params={"command": command}
        )

        return extract_output_from_stream(response)
    except Exception as e:
        return f"Error executing command: {e!s}"

```
  
---|---  
###  aexecute_command `async` [#](https://developers.llamaindex.ai/python/framework-api-reference/tools/aws_bedrock_agentcore/#llama_index.tools.aws_bedrock_agentcore.AgentCoreCodeInterpreterToolSpec.aexecute_command "Permanent link")
```
aexecute_command(command: , thread_id:  = 'default') -> 

```

Execute a shell command in the code interpreter sandbox (asynchronous version).
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`command` |  The command to execute. |  _required_  
`thread_id` |  Thread ID for the code interpreter session. Default is "default". |  `'default'`  
Returns:
Name | Type | Description  
---|---|---  
`str` |  The result of the command execution.  
Source code in `llama_index/tools/aws_bedrock_agentcore/code_interpreter/base.py`
```
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
```
| ```
async def aexecute_command(
    self,
    command: str,
    thread_id: str = "default",
) -> str:
"""
    Execute a shell command in the code interpreter sandbox (asynchronous version).

    Args:
        command (str): The command to execute.
        thread_id (str): Thread ID for the code interpreter session. Default is "default".

    Returns:
        str: The result of the command execution.

    """
    # Use the synchronous version as the underlying API is thread-safe
    return self.execute_command(command=command, thread_id=thread_id)

```
  
---|---  
###  read_files [#](https://developers.llamaindex.ai/python/framework-api-reference/tools/aws_bedrock_agentcore/#llama_index.tools.aws_bedrock_agentcore.AgentCoreCodeInterpreterToolSpec.read_files "Permanent link")
```
read_files(paths: [], thread_id:  = 'default') -> 

```

Read content of files in the environment (synchronous version).
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`paths` |  `List[str]` |  List of file paths to read. |  _required_  
`thread_id` |  Thread ID for the code interpreter session. Default is "default". |  `'default'`  
Returns:
Name | Type | Description  
---|---|---  
`str` |  The content of the files.  
Source code in `llama_index/tools/aws_bedrock_agentcore/code_interpreter/base.py`
```
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
```
| ```
def read_files(
    self,
    paths: List[str],
    thread_id: str = "default",
) -> str:
"""
    Read content of files in the environment (synchronous version).

    Args:
        paths (List[str]): List of file paths to read.
        thread_id (str): Thread ID for the code interpreter session. Default is "default".

    Returns:
        str: The content of the files.

    """
    try:
        # Get or create code interpreter
        code_interpreter = self._get_or_create_interpreter(thread_id=thread_id)

        # Read files
        response = code_interpreter.invoke(
            method="readFiles", params={"paths": paths}
        )

        return extract_output_from_stream(response)
    except Exception as e:
        return f"Error reading files: {e!s}"

```
  
---|---  
###  aread_files `async` [#](https://developers.llamaindex.ai/python/framework-api-reference/tools/aws_bedrock_agentcore/#llama_index.tools.aws_bedrock_agentcore.AgentCoreCodeInterpreterToolSpec.aread_files "Permanent link")
```
aread_files(paths: [], thread_id:  = 'default') -> 

```

Read content of files in the environment (asynchronous version).
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`paths` |  `List[str]` |  List of file paths to read. |  _required_  
`thread_id` |  Thread ID for the code interpreter session. Default is "default". |  `'default'`  
Returns:
Name | Type | Description  
---|---|---  
`str` |  The content of the files.  
Source code in `llama_index/tools/aws_bedrock_agentcore/code_interpreter/base.py`
```
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
```
| ```
async def aread_files(
    self,
    paths: List[str],
    thread_id: str = "default",
) -> str:
"""
    Read content of files in the environment (asynchronous version).

    Args:
        paths (List[str]): List of file paths to read.
        thread_id (str): Thread ID for the code interpreter session. Default is "default".

    Returns:
        str: The content of the files.

    """
    # Use the synchronous version as the underlying API is thread-safe
    return self.read_files(paths=paths, thread_id=thread_id)

```
  
---|---  
###  list_files [#](https://developers.llamaindex.ai/python/framework-api-reference/tools/aws_bedrock_agentcore/#llama_index.tools.aws_bedrock_agentcore.AgentCoreCodeInterpreterToolSpec.list_files "Permanent link")
```
list_files(directory_path:  = '', thread_id:  = 'default') -> 

```

List files in directories in the environment (synchronous version).
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`directory_path` |  Path to the directory to list. Default is current directory.  
`thread_id` |  Thread ID for the code interpreter session. Default is "default". |  `'default'`  
Returns:
Name | Type | Description  
---|---|---  
`str` |  The list of files.  
Source code in `llama_index/tools/aws_bedrock_agentcore/code_interpreter/base.py`
```
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
```
| ```
def list_files(
    self,
    directory_path: str = "",
    thread_id: str = "default",
) -> str:
"""
    List files in directories in the environment (synchronous version).

    Args:
        directory_path (str): Path to the directory to list. Default is current directory.
        thread_id (str): Thread ID for the code interpreter session. Default is "default".

    Returns:
        str: The list of files.

    """
    try:
        # Get or create code interpreter
        code_interpreter = self._get_or_create_interpreter(thread_id=thread_id)

        # List files
        response = code_interpreter.invoke(
            method="listFiles", params={"directoryPath": directory_path}
        )

        return extract_output_from_stream(response)
    except Exception as e:
        return f"Error listing files: {e!s}"

```
  
---|---  
###  alist_files `async` [#](https://developers.llamaindex.ai/python/framework-api-reference/tools/aws_bedrock_agentcore/#llama_index.tools.aws_bedrock_agentcore.AgentCoreCodeInterpreterToolSpec.alist_files "Permanent link")
```
alist_files(directory_path:  = '', thread_id:  = 'default') -> 

```

List files in directories in the environment (asynchronous version).
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`directory_path` |  Path to the directory to list. Default is current directory.  
`thread_id` |  Thread ID for the code interpreter session. Default is "default". |  `'default'`  
Returns:
Name | Type | Description  
---|---|---  
`str` |  The list of files.  
Source code in `llama_index/tools/aws_bedrock_agentcore/code_interpreter/base.py`
```
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
```
| ```
async def alist_files(
    self,
    directory_path: str = "",
    thread_id: str = "default",
) -> str:
"""
    List files in directories in the environment (asynchronous version).

    Args:
        directory_path (str): Path to the directory to list. Default is current directory.
        thread_id (str): Thread ID for the code interpreter session. Default is "default".

    Returns:
        str: The list of files.

    """
    # Use the synchronous version as the underlying API is thread-safe
    return self.list_files(directory_path=directory_path, thread_id=thread_id)

```
  
---|---  
###  delete_files [#](https://developers.llamaindex.ai/python/framework-api-reference/tools/aws_bedrock_agentcore/#llama_index.tools.aws_bedrock_agentcore.AgentCoreCodeInterpreterToolSpec.delete_files "Permanent link")
```
delete_files(paths: [], thread_id:  = 'default') -> 

```

Remove files from the environment (synchronous version).
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`paths` |  `List[str]` |  List of file paths to delete. |  _required_  
`thread_id` |  Thread ID for the code interpreter session. Default is "default". |  `'default'`  
Returns:
Name | Type | Description  
---|---|---  
`str` |  The result of the delete operation.  
Source code in `llama_index/tools/aws_bedrock_agentcore/code_interpreter/base.py`
```
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
```
| ```
def delete_files(
    self,
    paths: List[str],
    thread_id: str = "default",
) -> str:
"""
    Remove files from the environment (synchronous version).

    Args:
        paths (List[str]): List of file paths to delete.
        thread_id (str): Thread ID for the code interpreter session. Default is "default".

    Returns:
        str: The result of the delete operation.

    """
    try:
        # Get or create code interpreter
        code_interpreter = self._get_or_create_interpreter(thread_id=thread_id)

        # Remove files
        response = code_interpreter.invoke(
            method="removeFiles", params={"paths": paths}
        )

        return extract_output_from_stream(response)
    except Exception as e:
        return f"Error deleting files: {e!s}"

```
  
---|---  
###  adelete_files `async` [#](https://developers.llamaindex.ai/python/framework-api-reference/tools/aws_bedrock_agentcore/#llama_index.tools.aws_bedrock_agentcore.AgentCoreCodeInterpreterToolSpec.adelete_files "Permanent link")
```
adelete_files(paths: [], thread_id:  = 'default') -> 

```

Remove files from the environment (asynchronous version).
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`paths` |  `List[str]` |  List of file paths to delete. |  _required_  
`thread_id` |  Thread ID for the code interpreter session. Default is "default". |  `'default'`  
Returns:
Name | Type | Description  
---|---|---  
`str` |  The result of the delete operation.  
Source code in `llama_index/tools/aws_bedrock_agentcore/code_interpreter/base.py`
```
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
```
| ```
async def adelete_files(
    self,
    paths: List[str],
    thread_id: str = "default",
) -> str:
"""
    Remove files from the environment (asynchronous version).

    Args:
        paths (List[str]): List of file paths to delete.
        thread_id (str): Thread ID for the code interpreter session. Default is "default".

    Returns:
        str: The result of the delete operation.

    """
    # Use the synchronous version as the underlying API is thread-safe
    return self.delete_files(paths=paths, thread_id=thread_id)

```
  
---|---  
###  write_files [#](https://developers.llamaindex.ai/python/framework-api-reference/tools/aws_bedrock_agentcore/#llama_index.tools.aws_bedrock_agentcore.AgentCoreCodeInterpreterToolSpec.write_files "Permanent link")
```
write_files(files: [[, ]], thread_id:  = 'default') -> 

```

Create or update files in the environment (synchronous version).
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`files` |  `List[Dict[str, str]]` |  List of dictionaries with path and text fields. |  _required_  
`thread_id` |  Thread ID for the code interpreter session. Default is "default". |  `'default'`  
Returns:
Name | Type | Description  
---|---|---  
`str` |  The result of the write operation.  
Source code in `llama_index/tools/aws_bedrock_agentcore/code_interpreter/base.py`
```
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
```
| ```
def write_files(
    self,
    files: List[Dict[str, str]],
    thread_id: str = "default",
) -> str:
"""
    Create or update files in the environment (synchronous version).

    Args:
        files (List[Dict[str, str]]): List of dictionaries with path and text fields.
        thread_id (str): Thread ID for the code interpreter session. Default is "default".

    Returns:
        str: The result of the write operation.

    """
    try:
        # Get or create code interpreter
        code_interpreter = self._get_or_create_interpreter(thread_id=thread_id)

        # Write files
        response = code_interpreter.invoke(
            method="writeFiles", params={"content": files}
        )

        return extract_output_from_stream(response)
    except Exception as e:
        return f"Error writing files: {e!s}"

```
  
---|---  
###  awrite_files `async` [#](https://developers.llamaindex.ai/python/framework-api-reference/tools/aws_bedrock_agentcore/#llama_index.tools.aws_bedrock_agentcore.AgentCoreCodeInterpreterToolSpec.awrite_files "Permanent link")
```
awrite_files(files: [[, ]], thread_id:  = 'default') -> 

```

Create or update files in the environment (asynchronous version).
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`files` |  `List[Dict[str, str]]` |  List of dictionaries with path and text fields. |  _required_  
`thread_id` |  Thread ID for the code interpreter session. Default is "default". |  `'default'`  
Returns:
Name | Type | Description  
---|---|---  
`str` |  The result of the write operation.  
Source code in `llama_index/tools/aws_bedrock_agentcore/code_interpreter/base.py`
```
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
```
| ```
async def awrite_files(
    self,
    files: List[Dict[str, str]],
    thread_id: str = "default",
) -> str:
"""
    Create or update files in the environment (asynchronous version).

    Args:
        files (List[Dict[str, str]]): List of dictionaries with path and text fields.
        thread_id (str): Thread ID for the code interpreter session. Default is "default".

    Returns:
        str: The result of the write operation.

    """
    # Use the synchronous version as the underlying API is thread-safe
    return self.write_files(files=files, thread_id=thread_id)

```
  
---|---  
###  start_command [#](https://developers.llamaindex.ai/python/framework-api-reference/tools/aws_bedrock_agentcore/#llama_index.tools.aws_bedrock_agentcore.AgentCoreCodeInterpreterToolSpec.start_command "Permanent link")
```
start_command(command: , thread_id:  = 'default') -> 

```

Start a long-running command asynchronously (synchronous version).
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`command` |  The command to execute asynchronously. |  _required_  
`thread_id` |  Thread ID for the code interpreter session. Default is "default". |  `'default'`  
Returns:
Name | Type | Description  
---|---|---  
`str` |  The task ID and status.  
Source code in `llama_index/tools/aws_bedrock_agentcore/code_interpreter/base.py`
```
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
```
| ```
def start_command(
    self,
    command: str,
    thread_id: str = "default",
) -> str:
"""
    Start a long-running command asynchronously (synchronous version).

    Args:
        command (str): The command to execute asynchronously.
        thread_id (str): Thread ID for the code interpreter session. Default is "default".

    Returns:
        str: The task ID and status.

    """
    try:
        # Get or create code interpreter
        code_interpreter = self._get_or_create_interpreter(thread_id=thread_id)

        # Start command execution
        response = code_interpreter.invoke(
            method="startCommandExecution", params={"command": command}
        )

        return extract_output_from_stream(response)
    except Exception as e:
        return f"Error starting command: {e!s}"

```
  
---|---  
###  astart_command `async` [#](https://developers.llamaindex.ai/python/framework-api-reference/tools/aws_bedrock_agentcore/#llama_index.tools.aws_bedrock_agentcore.AgentCoreCodeInterpreterToolSpec.astart_command "Permanent link")
```
astart_command(command: , thread_id:  = 'default') -> 

```

Start a long-running command asynchronously (asynchronous version).
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`command` |  The command to execute asynchronously. |  _required_  
`thread_id` |  Thread ID for the code interpreter session. Default is "default". |  `'default'`  
Returns:
Name | Type | Description  
---|---|---  
`str` |  The task ID and status.  
Source code in `llama_index/tools/aws_bedrock_agentcore/code_interpreter/base.py`
```
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
```
| ```
async def astart_command(
    self,
    command: str,
    thread_id: str = "default",
) -> str:
"""
    Start a long-running command asynchronously (asynchronous version).

    Args:
        command (str): The command to execute asynchronously.
        thread_id (str): Thread ID for the code interpreter session. Default is "default".

    Returns:
        str: The task ID and status.

    """
    # Use the synchronous version as the underlying API is thread-safe
    return self.start_command(command=command, thread_id=thread_id)

```
  
---|---  
###  get_task [#](https://developers.llamaindex.ai/python/framework-api-reference/tools/aws_bedrock_agentcore/#llama_index.tools.aws_bedrock_agentcore.AgentCoreCodeInterpreterToolSpec.get_task "Permanent link")
```
get_task(task_id: , thread_id:  = 'default') -> 

```

Check status of an async task (synchronous version).
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`task_id` |  The ID of the task to check. |  _required_  
`thread_id` |  Thread ID for the code interpreter session. Default is "default". |  `'default'`  
Returns:
Name | Type | Description  
---|---|---  
`str` |  The task status.  
Source code in `llama_index/tools/aws_bedrock_agentcore/code_interpreter/base.py`
```
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
```
| ```
def get_task(
    self,
    task_id: str,
    thread_id: str = "default",
) -> str:
"""
    Check status of an async task (synchronous version).

    Args:
        task_id (str): The ID of the task to check.
        thread_id (str): Thread ID for the code interpreter session. Default is "default".

    Returns:
        str: The task status.

    """
    try:
        # Get or create code interpreter
        code_interpreter = self._get_or_create_interpreter(thread_id=thread_id)

        # Get task status
        response = code_interpreter.invoke(
            method="getTask", params={"taskId": task_id}
        )

        return extract_output_from_stream(response)
    except Exception as e:
        return f"Error getting task status: {e!s}"

```
  
---|---  
###  aget_task `async` [#](https://developers.llamaindex.ai/python/framework-api-reference/tools/aws_bedrock_agentcore/#llama_index.tools.aws_bedrock_agentcore.AgentCoreCodeInterpreterToolSpec.aget_task "Permanent link")
```
aget_task(task_id: , thread_id:  = 'default') -> 

```

Check status of an async task (asynchronous version).
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`task_id` |  The ID of the task to check. |  _required_  
`thread_id` |  Thread ID for the code interpreter session. Default is "default". |  `'default'`  
Returns:
Name | Type | Description  
---|---|---  
`str` |  The task status.  
Source code in `llama_index/tools/aws_bedrock_agentcore/code_interpreter/base.py`
```
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
```
| ```
async def aget_task(
    self,
    task_id: str,
    thread_id: str = "default",
) -> str:
"""
    Check status of an async task (asynchronous version).

    Args:
        task_id (str): The ID of the task to check.
        thread_id (str): Thread ID for the code interpreter session. Default is "default".

    Returns:
        str: The task status.

    """
    # Use the synchronous version as the underlying API is thread-safe
    return self.get_task(task_id=task_id, thread_id=thread_id)

```
  
---|---  
###  stop_task [#](https://developers.llamaindex.ai/python/framework-api-reference/tools/aws_bedrock_agentcore/#llama_index.tools.aws_bedrock_agentcore.AgentCoreCodeInterpreterToolSpec.stop_task "Permanent link")
```
stop_task(task_id: , thread_id:  = 'default') -> 

```

Stop a running task (synchronous version).
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`task_id` |  The ID of the task to stop. |  _required_  
`thread_id` |  Thread ID for the code interpreter session. Default is "default". |  `'default'`  
Returns:
Name | Type | Description  
---|---|---  
`str` |  The result of the stop operation.  
Source code in `llama_index/tools/aws_bedrock_agentcore/code_interpreter/base.py`
```
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
```
| ```
def stop_task(
    self,
    task_id: str,
    thread_id: str = "default",
) -> str:
"""
    Stop a running task (synchronous version).

    Args:
        task_id (str): The ID of the task to stop.
        thread_id (str): Thread ID for the code interpreter session. Default is "default".

    Returns:
        str: The result of the stop operation.

    """
    try:
        # Get or create code interpreter
        code_interpreter = self._get_or_create_interpreter(thread_id=thread_id)

        # Stop task
        response = code_interpreter.invoke(
            method="stopTask", params={"taskId": task_id}
        )

        return extract_output_from_stream(response)
    except Exception as e:
        return f"Error stopping task: {e!s}"

```
  
---|---  
###  astop_task `async` [#](https://developers.llamaindex.ai/python/framework-api-reference/tools/aws_bedrock_agentcore/#llama_index.tools.aws_bedrock_agentcore.AgentCoreCodeInterpreterToolSpec.astop_task "Permanent link")
```
astop_task(task_id: , thread_id:  = 'default') -> 

```

Stop a running task (asynchronous version).
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`task_id` |  The ID of the task to stop. |  _required_  
`thread_id` |  Thread ID for the code interpreter session. Default is "default". |  `'default'`  
Returns:
Name | Type | Description  
---|---|---  
`str` |  The result of the stop operation.  
Source code in `llama_index/tools/aws_bedrock_agentcore/code_interpreter/base.py`
```
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
```
| ```
async def astop_task(
    self,
    task_id: str,
    thread_id: str = "default",
) -> str:
"""
    Stop a running task (asynchronous version).

    Args:
        task_id (str): The ID of the task to stop.
        thread_id (str): Thread ID for the code interpreter session. Default is "default".

    Returns:
        str: The result of the stop operation.

    """
    # Use the synchronous version as the underlying API is thread-safe
    return self.stop_task(task_id=task_id, thread_id=thread_id)

```
  
---|---  
###  cleanup `async` [#](https://developers.llamaindex.ai/python/framework-api-reference/tools/aws_bedrock_agentcore/#llama_index.tools.aws_bedrock_agentcore.AgentCoreCodeInterpreterToolSpec.cleanup "Permanent link")
```
cleanup(thread_id: Optional[] = None) -> None

```

Clean up resources
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`thread_id` |  `Optional[str]` |  Optional thread ID to clean up. If None, cleans up all sessions. |  `None`  
Source code in `llama_index/tools/aws_bedrock_agentcore/code_interpreter/base.py`
```
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
```
| ```
async def cleanup(self, thread_id: Optional[str] = None) -> None:
"""
    Clean up resources

    Args:
        thread_id: Optional thread ID to clean up. If None, cleans up all sessions.

    """
    if thread_id:
        # Clean up a specific thread's session
        if thread_id in self._code_interpreters:
            try:
                self._code_interpreters[thread_id].stop()
                del self._code_interpreters[thread_id]
                logger.info(
                    f"Code interpreter session for thread {thread_id} cleaned up"
                )
            except Exception as e:
                logger.warning(
                    f"Error stopping code interpreter for thread {thread_id}: {e}"
                )
    else:
        # Clean up all sessions
        thread_ids = list(self._code_interpreters.keys())
        for tid in thread_ids:
            try:
                self._code_interpreters[tid].stop()
            except Exception as e:
                logger.warning(
                    f"Error stopping code interpreter for thread {tid}: {e}"
                )

        self._code_interpreters = {}
        logger.info("All code interpreter sessions cleaned up")

```
  
---|---  
options: members: - AgentCoreBrowserToolSpec - AgentCoreCodeInterpreterToolSpec
