import aiohttp
from typing import Any, Dict, Optional

async def base_network_service(
url: str,
method: str = "GET",
body: Optional[Dict] = None,
query: Optional[Dict] = None,
headers: Optional[Dict] = None
) -> Any:
    """
    공통 API 요청 헬퍼 (GET, POST, DELETE 등 지원)

    Args:
        url: 요청 URL
        method: HTTP 메소드 ("GET", "POST", "DELETE" 등)
        data: POST/DELETE 요청 시 JSON 바디
        params: GET/DELETE 요청 시 쿼리 파라미터
    """
    try: 
        timeout = aiohttp.ClientTimeout(total=10) 
        
        async with aiohttp.ClientSession(timeout=timeout, headers=headers) as session: 
            method = method.upper() 
            if method == "GET": 
                async with session.get(url, params=query) as response: 
                    response.raise_for_status() 
                    
                    return await response.json() 
                
            elif method == "POST": 
                async with session.post(url, json=body, params=query) as response: 
                    response.raise_for_status() 
                    
                    return await response.json() 
                
            elif method == "DELETE": 
                async with session.delete(url, json=body, params=query) as response: 
                    response.raise_for_status() 
                    
                    return await response.json() 
            
            else: 
                raise ValueError(f"지원하지 않는 HTTP 메서드: {method}") 
            
    except aiohttp.ClientResponseError as e: 
        print(f"HTTP 상태 코드 오류: {e.status} - {e.message}") 
        raise 
    except aiohttp.ClientError as e: 
        print(f"API 요청 실패: {e}") 
        raise 
    except Exception as e: 
        print(f"알 수 없는 에러 발생: {e}") 
        raise