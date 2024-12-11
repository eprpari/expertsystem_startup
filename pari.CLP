(deftemplate selected-industry 
   (slot industry)           
)

(deftemplate regulatory-requirement
   (slot industry)
   (slot requirements)  
)

(deftemplate recommended-location
   (slot industry)        
   (slot location)        
   (slot suitability-factors) 
)

(deftemplate recommended-location
   (slot industry)         ; Industry for the recommended location
   (slot location)         ; Location name
   (slot suitability-factors)  ; Factors that make this location ideal for the industry
)

(deftemplate funding-recommendation
   (slot industry)
   (slot sources))  ; List of funding sources



(defrule location-analysis
   (selected-industry (industry ?industry))  ; Accessing the industry from selected-industry fact
   =>
   (if (eq ?industry  tech) then
      (assert (recommended-location (industry tech) (location Colombo) (suitability-factors "Advanced infrastructure and access to skilled labor.")))
      (assert (recommended-location (industry tech) (location Kandy) (suitability-factors "Growing tech community and educational institutions.")))
      (assert (recommended-location (industry tech) (location Jaffna) (suitability-factors "Emerging tech scene and access to affordable labor.")))
   )
   (if (eq ?industry tourism) then
      (assert (recommended-location (industry tourism) (location Galle) (suitability-factors "Popular tourist destination with historical significance.")))
      (assert (recommended-location (industry tourism) (location Colombo) (suitability-factors "Major international gateway, ideal for high-end tourism.")))
      (assert (recommended-location (industry tourism) (location Negombo) (suitability-factors "Accessible to international tourists, with a beach resort feel.")))
   )
   (if (eq ?industry retail) then
      (assert (recommended-location (industry retail) (location Colombo) (suitability-factors "High population density and well-established shopping centers.")))
      (assert (recommended-location (industry retail) (location Negombo) (suitability-factors "High customer footfall due to tourism.")))
      (assert (recommended-location (industry retail) (location Kandy) (suitability-factors "Tourist traffic combined with a growing local market.")))
   )
)

(defrule regulatory-compliance
   (selected-industry (industry ?industry))  ; Trigger based on selected industry
   =>
   (if (eq ?industry tech) then
      (assert (regulatory-requirement 
                 (industry tech) 
                 (requirements "Tech Industry Approval, Data Protection Certification, Cybersecurity Compliance"))))

   (if (eq ?industry tourism) then
      (assert (regulatory-requirement 
                 (industry tourism) 
                 (requirements "Tourism Board Approval, Health and Safety Certification, Business Registration"))))

   (if (eq ?industry retail) then
      (assert (regulatory-requirement 
                 (industry retail) 
                 (requirements "Trade License, Business Registration, Local Municipality Approval"))))
)

(defrule funding-advice
   (selected-industry (industry ?industry))  ; Trigger based on the selected industry
   =>
   (if (eq ?industry tech) then
      (assert (funding-recommendation 
               (industry tech) 
               (sources "Angel Investors, Venture Capital, Startup Accelerators"))))
   
   (if (eq ?industry tourism) then
      (assert (funding-recommendation 
               (industry tourism) 
               (sources "Government Grants, Tourism Development Funds, Bank Loans"))))
   
   (if (eq ?industry retail) then
      (assert (funding-recommendation 
               (industry retail) 
               (sources "Microfinance, Crowdfunding, Friends and Family")))))


